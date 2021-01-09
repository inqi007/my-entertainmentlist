from django.shortcuts import render
import requests
from .models import Favorites, Towatch
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def main(request):
    showsnow = Favorites.objects.filter(username=request.user).order_by('name')
    showslater = Towatch.objects.filter(user=request.user).order_by('title')
    return render(request, "account/users.html", {
        "favorites": showsnow,
        "later": showslater
    })

def search(request):
    if request.method == "POST":
        query = request.POST.get('search')
        response = requests.get(f'https://api.jikan.moe/v3/search/anime?q={query}')
        data = response.json()
        return render(request, "account/anime.html", {
            "results": data['results']  
        })
    
    response = requests.get('https://api.jikan.moe/v3/top/anime')
    data = response.json()
    return render(request, "account/anime.html", {
        "results": data['top']
    })

def add(request):
    title = request.POST.get('title')
    title_d = Favorites.objects.create(name=title, username=request.user)
    return HttpResponseRedirect(reverse("main"))

def remove(request):
    title = request.POST.get('delete')
    later = request.POST.get('delete1')
    Favorites.objects.filter(name=title).filter(username=request.user).delete()
    Towatch.objects.filter(title=later).filter(user=request.user).delete()
    
    return HttpResponseRedirect(reverse("main"))

def later(request):
    title = request.POST.get('watchlater')
    Towatch.objects.create(user=request.user, title=title)
    return HttpResponseRedirect(reverse("main"))

def next(request):
    if request.method=="POST":
        response = requests.get('https://api.jikan.moe/v3/top/anime/2')
        data = response.json()
        return render(request, "account/anime.html", {
            "results": data['top']
        })
        

