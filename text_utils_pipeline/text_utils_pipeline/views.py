# I have created this file - Pirih Sahito

from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlineremover(request):
    return HttpResponse("New Line Remover")

def spaceremover(request):
    return HttpResponse("Space Remover")

def charcount(request):
    return HttpResponse("Characters Counter")