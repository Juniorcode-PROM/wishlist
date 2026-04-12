from django.contrib.auth.models import User
from django.db.transaction import commit
from django.shortcuts import render, redirect

from main.models import Item
from main.forms import RegisterForm, Add_Vishlist
from main.models import Item


def prof(request,username):
    items=Item.objects.filter(author__username=username)
    return render(request,"profile.html",{"items":items,"username":username})


def home(request):
    if request.user.is_authenticated:
        return redirect(f"/profile/{request.user.username}/")
    else:
        return redirect("/login/")


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


def create_vish(request):
    if request.method == "POST":
        form = Add_Vishlist(request.POST)
        if form.is_valid():
            vish = Item.object.create(
                name=form.cleaned_data["predmet"],
                author=request.user
            )
            return redirect(f"/profile/{request.user.username}/")
    else:
        form = Add_Vishlist()
    return render(request, "create_vish.html", {
        "form": form
    })
