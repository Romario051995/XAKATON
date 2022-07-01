from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("", task_list, name='home'),
    path("task_detail/<int:task_id>/", task_detail, name='task_detail')
]