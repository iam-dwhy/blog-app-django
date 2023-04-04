import datetime
from django.shortcuts import render
from .models import Blog


def current_datetime(request):
    now = datetime.datetime.now()

    context = {
        'date': now,
        'name': "diya"
    }

    return render(request, 'index.html', context)



def get_blogs(request):
    # get all the blogs from our database
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }

    return render(request, 'blog_all.html', context)