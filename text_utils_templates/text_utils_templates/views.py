# I have created this file - Pirih Sahito

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name' : 'Pirih Sahito', 'place' : 'Pluto'}
    return render(request, 'index.html', params)