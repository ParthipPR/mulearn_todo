from django.urls import path
from . import views

urlpatterns = [
    path('updatepage/<int:task_id>/', views.updatepage, name='api_updatepage'),
    path('tasks/', views.tasks, name='api_tasks'),
    path('completed/<int:task_id>/', views.completed, name='api_completed'),
    path('delete/<int:task_id>/', views.delete, name='api_delete'),
    path('add_task/', views.add_task, name='api_add_task'),
    path('update/<int:task_id>/', views.update, name='api_update'),
    path('register/', views.register, name='api_register'),
    path('login/', views.login, name='api_login'),
    path('logout/', views.logout, name='api_logout'),
]
