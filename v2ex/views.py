import hashlib
from django.shortcuts import render, redirect
from v2ex.models import Category, Tag, Topic, UserProfile

from v2ex.forms import UserForm
from django import forms
from django.contrib.auth.models import User

def index(request):
    categorys = Category.objects.all()
    display = request.GET.get('display','')
    if not display:
        display = request.COOKIES.get('display','8')
    c = Category.objects.get(id=int(display))
    tags = Tag.objects.filter(category=c).all()
    topics = Topic.objects.filter(tag__category=c).all()
    context_dict = {
        'categorys':categorys,
        'tags':tags,
        'c':c,
        'topics': topics,
    }
    response =  render(request,'index.html',context_dict)
    response.set_cookie('display',display)

    return response

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.data.get('username'), email=form.data.get('email'), password=form.data.get('password'))
            user.set_password(user.password)
            user.save()
            up = UserProfile(user=user, avatar_hash=hashlib.md5(user.email.encode('utf-8')).hexdigest())
            up.save()
        return redirect('index')
    return render(request, 'user/user_register.html', {'form':form})

