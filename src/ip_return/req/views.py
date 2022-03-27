from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def ip_address(request):
    template = 'req/base.html'
    
    name = ''
    if request.GET.get('name'):
        name = request.GET.get('name')
    

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    dict = {'ip': ip}
    jsondata = json.dumps(dict)
    #print(jsondata)
    
    context = {
        'data': jsondata,
        'name': name
    }
    
    return render(request, template, context)
