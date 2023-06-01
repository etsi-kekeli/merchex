from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Champion ! Keep learning ! </h1>")

def about(request):
    return HttpResponse(
        """<h1>A propos de nous</h1>
        <p>Qu'est-ce que nous adorons merchex !</p>"""
    )

def listings(request):
    return HttpResponse(
        """
        <h1>Listings</h1>
        <p>Awesome products ! We have plenty of them !</p>
        """
    )

def contact(request):
    return HttpResponse(
        """
        <h1>Contact us</h1>
        <form method='POST'>

        </form>
        """
    )