from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def manas(request):
    return HttpResponse("<marquee><h1> har har mahadev</h1></marquee>")
