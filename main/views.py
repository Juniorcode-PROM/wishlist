from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.transaction import commit
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Item
from main.forms import RegisterForm, Add_Vishlist
from main.models import Item


def prof(request, username):
    items = Item.objects.filter(author__username=username)
    return render(
        request, "profile.html", {"items": items, "username": username}
    )


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

@login_required
def create_vish(request):
    if request.method == "POST":
        form = Add_Vishlist(request.POST)
        if form.is_valid():
            vish = Item.objects.create(
                name=form.cleaned_data["predmet"],
                author=request.user
            )
            return redirect(f"/profile/{request.user.username}/")
    else:
        form = Add_Vishlist()
    return render(
        request, "create_vish.html", {
            "form": form
        }
    )

@login_required
def delete(request, Item_id):
    item = get_object_or_404(Item, pk=Item_id)
    ctx = {"item": item}

    if request.method == "POST":
        ath = request.user.id
        if item.author.id == ath:
            item.delete()
            return redirect(f"/profile/{request.user.username}")
        else:
            ctx |= {"err": "Нет прав"}
            return render(request, "delete_item.html", ctx)

    else:
        return render(request, "delete_item.html")


@login_required
def pick_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    ctx = {"item": item}
    if request.method == "POST":
        if item.picked:
            ctx |= {"err": "Уже выбран"}
            return render(request, "pick_item.html", ctx)
        else:
            item.picked = request.user
            item.save()
            return redirect(f"/profile/{item.author.username}/")
    else:
        return render(request, "pick_item.html", ctx)
