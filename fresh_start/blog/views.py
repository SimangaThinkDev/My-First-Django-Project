from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

# Create your views here.

posts = [
    {
        "Author": "Teko Modise",
        "Title": "A Retired Football Icon",
        "Content": "Teko Tsholofelo Modise (born 22 December 1982), \
        nicknamed The General and Techno M, is a South African retired professional footballer, \
        former Bafana Bafana captain who played as a midfielder and who is currently \
        a staff member at Cape Town City Football Club.",
        "Date": f"28 September 2023"
    },
    {
        "Author": "Katlego Mphela",
        "Title": "Another Retired Football Icon",
        "Content": "Mphela, a product of Jomo Cosmos, \
        played in France for RC Strasbourg Alsace and Stade de Reims, both with limited success. \
        After returning home he turned out for SuperSport United for the 2007 to 08 \
        season before joining Mamelodi Sundowns the following season. \
        He then finished the 2009 to 10 season with 17 goals in 30 games \
        which made him the league's top goalscorer. He won the \
        Lesley Manyathela Golden Boot and was voted PSL Players Player of the Season.",
        "Date": f"27 September 2023"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, "blog/about.html", {"title": "About"})