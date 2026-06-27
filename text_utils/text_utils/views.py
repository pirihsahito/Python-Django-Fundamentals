# I have created this file - Pirih Sahito

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Text Utils Home</h1>")

def about(request):
    return HttpResponse("About Text Utils Engine")