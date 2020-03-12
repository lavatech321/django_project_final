from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import TodoModel
from django.views.decorators.http import require_POST

def home(requests):
	records = TodoModel.objects.order_by('id')
	form = TodoForm()
	context = { 'record' : records , 'form': form }
	return render(requests,'working/2-todo.html' , context)
# Create your views here.


@require_POST
def addtodo(requests):
	print('Hi')
	record = TodoForm(requests.POST)
	print(record)
	if record.is_valid():
		record.save()
	return redirect('home')

def completeTodo(requests, todo_id):
	record = TodoModel.objects.get(id=todo_id)
	record.complete=True
	record.save()
	return redirect('home')

def delete_completed(requests):
	TodoModel.objects.filter(complete__exact=True).delete()
	return redirect('home')

def delete_all(requests):
	TodoModel.objects.all().delete()
	return redirect('home')	