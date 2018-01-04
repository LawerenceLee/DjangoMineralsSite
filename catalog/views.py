from random import choice

from django.shortcuts import get_object_or_404, redirect, render

from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'catalog/index.html', {"minerals": minerals})


def detail(request, mineral_name):
    mineral = get_object_or_404(Mineral, name=mineral_name)
    return render(request, "catalog/detail.html", {"mineral": mineral})


def random(request):
    minerals = Mineral.objects.all()
    mineral = choice(minerals)
    return redirect("/{}".format(mineral.name))
