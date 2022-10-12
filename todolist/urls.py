from django.urls import path
from todolist.views import change_task_status, delete_task, register,login_user,logout_user,show_todolist,create_task,show_json,add_task

app_name = 'todolist'

urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('',show_todolist,name='show_todolist'),
    path('create-task/',create_task,name='create-task'),
    path("change-task-status/<int:pk>/", change_task_status, name = "change-task-status"),
    path("delete-task/<int:pk>/", delete_task, name = "delete-task"),
    path('json/',show_json,name="show_json"),
    path('add/',add_task,name="add_task")


]