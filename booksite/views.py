from django.http import HttpResponse
import datetime

# Import some template processing methods
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render

# request is an object that contains information about the current web request
# that triggered this method, it is an instance of class 
# django.http.HttpRequest

# a View is a python function that takes an HttpRequest as a parameter
# and returns an HttpResponse
def hello(request):
    return HttpResponse("<h1>Hello World of Django!</h1>")
    

def current_datetime(request):
    now = datetime.datetime.now()    
    return render(request, 'current_datetime.html', {'current_date': now})
    
    
def hours_behind(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() - datetime.timedelta(hours=offset)
    return render(request, 'hours_behind.html', {'offset': offset, 'dt': dt})
    
# shows example of try-except, Http404 exception
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'offset':offset, 'dt':dt})
    
def display_meta(request):
    values = list(request.META.items())
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
