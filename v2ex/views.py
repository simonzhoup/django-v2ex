from django.shortcuts import render
from v2ex.models import Category, Tag, Topic

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