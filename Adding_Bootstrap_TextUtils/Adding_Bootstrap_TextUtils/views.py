from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    analyzed = djtext

    # Check box values
    removepunc = request.GET.get('removepunc', 'off')
    allcaps = request.GET.get('allcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    purpose = []
    char_count = None

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-{}[]—;:'"\,<>./?@#$%^&*_...~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose.append('Removed Punctuations')
        djtext = analyzed

    if allcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose.append('Changed to uppercase')
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose.append('New Line Removed')
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            # Guard condition protects index + 1 from exceeding string length bounds
            if index + 1 < len(djtext):
                if not(djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
            else:
                analyzed = analyzed + char
        purpose.append('Extra Space Removed')
        djtext = analyzed

    if charcounter == "on":
        char_count = 0
        for char in djtext:
            if char != " ":
                char_count = char_count + 1
        purpose.append('Characters Counted (No Spaces)')

    if removepunc != "on" and allcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on":
        return HttpResponse("Please select any operation and try again")
    
    # Pack everything safely into the final context object
    params = {
        'purpose': ", ".join(purpose), 
        'analyzed_text': analyzed,
        'character_count': char_count
    }

    return render(request, 'analyze.html', params)