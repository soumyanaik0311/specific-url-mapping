from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def virat_kohli(request):
#     return HttpResponse("<h1><marquee>Virat Kohli is best batsman</h1></marquee>")

# def dhoni(request):
#     return HttpResponse("<h1><marquee>dhoni is best wicket-keeper</h1></marquee>")


def virat_kohli(request):
    return render(request, 'virat_kohli.html')

def dhoni(request):
    return render(request, 'dhoni.html')

