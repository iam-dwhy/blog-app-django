from django.http import HttpResponse
import datetime
from django.shortcuts import render



def current_datetime(request):
    now = datetime.datetime.now()

    context = {
        'date': now,
        'name': "diya"
    }

    return render(request, 'index.html', context)



def get_blogs(request):
    return render(request, 'blogs.html')