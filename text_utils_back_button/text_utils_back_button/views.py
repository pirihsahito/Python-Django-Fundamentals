# I have created this file - Pirih Sahito

from django.http import HttpResponse

def index(request):
    home = """
         <h3>Home</h3>
         <a href='http://127.0.0.1:8000/removepunc'>Punctuation Remover<br></a>
         <a href='http://127.0.0.1:8000/capitalizefirst'>Capitalize First<br></a>
         <a href='http://127.0.0.1:8000/newlineremover'>New Line Remover<br></a>
         <a href='http://127.0.0.1:8000/charcount'>Characters Count</a>
           """
    return HttpResponse(home)

def removepunc(request):
    return HttpResponse("Punctuation Remover <a href= '/'><br>Back</a>")

def capfirst(request):
    return HttpResponse("Capitalize First <a href= '/'><br>Back</a>")

def newlineremover(request):
    return HttpResponse("New Line Remover <a href= '/'><br>Back</a>")

def spaceremover(request):
    return HttpResponse("Space Remover <a href= '/'><br>Back</a>")

def charcount(request):
    return HttpResponse("Characters Count <a href= '/'><br>Back</a>")