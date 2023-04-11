import datetime
from django.http import Http404
from django.shortcuts import render
from .models import Blog


def current_datetime(request):
    now = datetime.datetime.now()

    context = {
        'date': now,
        'name': "diya"
    }

    return render(request, 'index.html', context)


# get all the blogs from our database
def get_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }


    return render(request, 'blog_all.html', context)


# this function gets a blog with ID
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
        context = {
            'blog': blog
        }
        return render(request, 'blog.html', context)
    
    except:
        raise Http404("Blog does not exist")




