
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! ~ Rango <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("About Rango <br/> <a href='/rango/'>Index</a>")

