from django.http import HttpResponse
import datetime



def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html> <body> the current date and time of this blogpost is {now} </body></html>" # make the html better
    return HttpResponse(html, status=201)



def get_blogs(request):

    return HttpResponse('No Blog ', status=404)