from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('addtodo/' , views.addtodo , name='addtodo'),
    path('completeTodo/<todo_id>', views.completeTodo, name='todo_complete'),
    path('deletecompleted/' , views.delete_completed , name='delete_completed'),
    path('deleteall/' , views.delete_all , name='delete_all'),
]
