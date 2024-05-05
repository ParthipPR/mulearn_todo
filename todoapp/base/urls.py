from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("signup/",views.signup,name="signup"),
    path("tasks/",views.tasks,name="tasks"),
    path("completed/<int:task_id>/", views.completed, name='completed'),
    path("delete/<int:task_id>/",views.delete,name="delete"),
    path("add_task/",views.add_task, name="add"),
    path("update_page/<int:task_id>/",views.updatepage, name="updatepage"),
    path("update/<int:task_id>/",views.update, name="update")
]