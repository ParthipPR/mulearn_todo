from django.urls import path
from . import views

urlpatterns = [
    path('updatepage/<int:task_id>/', views.updatepage, name='updatepage'),
    path('tasks/', views.tasks, name='tasks'),
    path('completed/<int:task_id>/', views.completed, name='completed'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('add_task/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
