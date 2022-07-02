from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("task_list/", task_list, name='task_list'),
    path("task_detail/<int:task_id>/", task_detail, name='task_detail'),
    path("login/", log_in ,  name="login"),
    path("logout/", log_out ,  name="logout"),
]