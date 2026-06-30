# I have created this file - Pirih Sahito

from django.http import HttpResponse

def navigate(request):
    n = """<h1>Navigation Bar<br></h1>
        <h4>Learn Django:</h4>
        <a href='https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>Harry's Python-Django Playlist<br></a>
        <h4>To access Facebook:</h4>
        <a href='https://www.facebook.com/'>Facebook.com<br></a>
        <h4>My GitHub Account:</h4>
        <a href='https://github.com/pirihsahito'>Pirih Sahito - GitHub Profile</a>"""
    return HttpResponse(n)