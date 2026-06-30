# I have created this file - Pirih Sahito

from django.http import HttpResponse

def index(request):
    home = """
         <a href='http://127.0.0.1:8000/'>Home<br></a>
         <a href='http://127.0.0.1:8000/removepunc'>Punctuation Remover<br></a>
         <a href='http://127.0.0.1:8000/capitalizefirst'>Capitalize First<br></a>
         <a href='http://127.0.0.1:8000/newlineremover'>New Line Remover<br></a>
         <a href='http://127.0.0.1:8000/charcount'>Characters Count</a>
           """
    return HttpResponse(home)

def removepunc(request):
    punc = """
         <a href='http://127.0.0.1:8000/'>Home</a>
         <h4>Punctuation Remover</h4>
           """
    return HttpResponse(punc)

def capfirst(request):
    capital = """
         <a href='http://127.0.0.1:8000/'>Home</a>
         <h4>Capitalize First</h4>
           """
    return HttpResponse(capital)

def newlineremover(request):
    newline = """
         <a href='http://127.0.0.1:8000/'>Home</a>
         <h4>New Line Remover</h4>
           """
    return HttpResponse(newline)

def spaceremover(request):
    space = """
         <a href='http://127.0.0.1:8000/'>Home</a>
         <h4>Space Remover</h4>
           """
    return HttpResponse(space)

def charcount(request):
    count = """
         <a href='http://127.0.0.1:8000/'>Home</a>
         <h4>Characters Count</h4>
           """
    return HttpResponse(count)