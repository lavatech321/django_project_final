
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team,Topic, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import NewTopicForm


def page1(request):
    all_obj = Team.objects.all()
    context = { 'team':all_obj }
    return render(request, 'page1.html', context)

def page2(request,teamname):
    tname = teamname
    tobj = Team.objects.get(name=teamname)
    topics = Topic.objects.filter(board=tobj)
    context = {'teamname':tname , 'topics':topics}
    return render(request,'page2.html',context)

def page3(request,tname):
    team = get_object_or_404(Team , name=tname)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            mytopic = form.save(commit=False)
            mytopic.board = team
            mytopic.starter = user
            mytopic.save()
            mycomment = Comment.objects.create(
                message=form.cleaned_data.get('message'),
                topic=mytopic,
                created_by=user
            )
            return redirect('page2', teamname=tname)
    else:
        form = NewTopicForm()
    context = {'teamname':tname , 'form':form}
    return render(request,'page3.html', context)

def page4(request):
    return render(request,'page4.html')

def page5(request):
    return render(request,'page5.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('page1')
    else:
        form = UserCreationForm()
    context = { 'form': form }
    return render(request,'signup.html', context)