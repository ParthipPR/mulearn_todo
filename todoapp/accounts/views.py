from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken ...')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                print("user added")
        else:
            messages.info(request,'Password not matching ...')
            return redirect('register')

        return redirect('login')

    else:
        return render(request,"signup.html")
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')