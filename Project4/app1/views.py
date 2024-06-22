from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def soumya(request):
    return HttpResponse("<h1><marquee>hii, I am soumya here</h1></marquee>")

def nilesh(request):
    return HttpResponse("<h1><marquee>hii, I am nilesh Here</h1></marquee>")
