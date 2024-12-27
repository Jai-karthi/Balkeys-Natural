from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
a = ['controversial surivilen tech sport debate in the uk ','controversial surivilen tech sport debate in the uk ','controversial surivilen tech sport debate in the uk ']
def index(request):
    # template = loader.get_template('base.html')
    # return HttpResponse(template.render())
    return render(request,'base.html',{'a':a})

def events(request):
    return render(request,'events.html')

def About(request):
    return render(request,'About.html')

l = [{'id':1,'a':'home app under construction '} , {'id':2 ,'a': 'events a'},]
def Exclusive(request,id):
    r = {'b' :None}
    for i in l:
        if id == i['id']:
            r = {'key' : i}
    return render(request,'Exculsive.html',r)
def News(request):
    return render(request,'News.html')