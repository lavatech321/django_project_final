from django.shortcuts import render
from save.models import CommentModel

# Create your views here.

def home(request):
	records = CommentModel.objects.order_by('-date_added')
	context = {'record' : records}
	return render(request,'display/home.html', context)