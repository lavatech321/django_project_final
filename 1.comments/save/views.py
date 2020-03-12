from django.shortcuts import render, redirect
from .forms import CommentForm

def signup(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			print('hi')
			return redirect('home')
		else:
			print(form.errors)
	else:
		form = CommentForm()
	context = { 'form' : form }
	return render(request,'save/save.html', context)
# Create your views here.
