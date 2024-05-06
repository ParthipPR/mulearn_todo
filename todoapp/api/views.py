from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import Task
from .serializers import TaskSerializer
from datetime import date

@api_view(['GET'])
def updatepage(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['GET'])
def tasks(request):
    today = date.today()
    user = request.user
    
    pending_tasks = Task.objects.filter(user=user, completed=False, deadline__gte=today)
    completed_tasks = Task.objects.filter(user=user, completed=True)
    expired_tasks = Task.objects.filter(user=user, completed=False, deadline__lt=today)

    tasks_count = pending_tasks.count() + completed_tasks.count() + expired_tasks.count()

    pending_serializer = TaskSerializer(pending_tasks, many=True)
    completed_serializer = TaskSerializer(completed_tasks, many=True)
    expired_serializer = TaskSerializer(expired_tasks, many=True)

    return Response({
        'pending_tasks': pending_serializer.data,
        'completed_tasks': completed_serializer.data,
        'expired_tasks': expired_serializer.data,
        'tasks': tasks_count
    })

@api_view(['POST'])
def completed(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    task_instance.completed = True
    task_instance.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    task_instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
