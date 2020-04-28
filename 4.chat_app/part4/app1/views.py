
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team,Topic, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import NewTopicForm, CommentForm
from django.utils import timezone

def page1(request):
    all_obj = Team.objects.all()
    context = { 'team':all_obj}
    return render(request, 'page1.html', context)


@login_required
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
                created_by=user,
                updated_by=user,
            )
            return redirect('page2', teamname=tname)
    else:
        form = NewTopicForm()
    context = {'teamname':tname , 'form':form}
    return render(request,'page3.html', context)

def page4(request,teamname,topic):
    # comments = get_object_or_404(Comment , topic__id=topic)
    comments = Comment.objects.filter(topic__id=topic)
    a_topic = comments[0].topic.subject
    context = { 'teamname':teamname , 'comments':comments, 'topic': a_topic}
    return render(request,'page4.html', context)

def page5(request,teamname,topic):
    topic = get_object_or_404(Topic , subject=topic)
    comments = Comment.objects.filter(topic__id=topic.pk)
    a_topic = comments[0].topic.subject
    id_topic = comments[0].topic.id
    form = CommentForm()
    context = { 'teamname':teamname , 'topic':topic , 'comments': comments , 'topic': a_topic , 'id_topic':id_topic , 'form':form}
    return render(request,'page5.html', context)


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


@login_required
def add_comment(request,tname,topic):
    team = get_object_or_404(Team , name=tname)
    mytopic = get_object_or_404(Topic , id=topic)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            mycomment = form.save(commit=False)
            mycomment.topic = mytopic
            mycomment.created_by = request.user
            mycomment.updated_by = request.user
            mycomment.updated_at = timezone.now()
            mycomment.save()

            mytopic.last_updated = timezone.now()
            mytopic.save()

            return redirect('page4', teamname=tname , topic=topic)
    else:
        form = CommentForm()
    topic = get_object_or_404(Topic , subject=topic)
    comments = Comment.objects.filter(topic__id=topic.pk)
    a_topic = comments[0].topic.subject
    id_topic = comments[0].topic.id
    context = { 'teamname':teamname , 'topic':topic , 'comments': comments , 'topic': a_topic , 'id_topic':id_topic, 'form':form}
    return render(request,'page5.html', context)

