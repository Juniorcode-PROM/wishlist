from django.shortcuts import render

from main.models import Item


# Create your views here.
def prof(request,username):
    items=Item.objects.filter(author__username=username)
    return render(request,"profile.html",{"items":items,"username":username})

