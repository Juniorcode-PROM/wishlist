from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from main.models import Item
from main.forms import RegisterForm


def prof(request,username):
    items=Item.objects.filter(author__username=username)
    return render(request,"profile.html",{"items":items,"username":username})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["login"],
                password=form.cleaned_data["password"]
            )
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
