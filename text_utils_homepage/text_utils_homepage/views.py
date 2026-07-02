# I have created this file - Pirih Sahito

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse("Remove Punctuation")
