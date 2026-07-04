# I have created this file - Pirih Sahito

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check box values
    removepunc = request.GET.get('removepunc', 'off')
    allcaps = request.GET.get('allcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-{}[]—;:'"\,<>./?@#$%^&*_...~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    elif allcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to uppercase', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose' : 'New Line Removed', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose' : 'Extra Space Removed', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    elif charcounter == "on":
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1
        params = {'purpose' : 'Characters Counted (No Spaces)', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")