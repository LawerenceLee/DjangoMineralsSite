from random import randint

from django.shortcuts import get_object_or_404, redirect, render

from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'catalog/index.html', {"minerals": minerals})


def detail(request, mineral_name):
    mineral = get_object_or_404(Mineral, name=mineral_name)
    return render(request, "catalog/detail.html", {"mineral": mineral})


def random(request):
    rand_num = randint(1, 873)
    mineral = get_object_or_404(Mineral, pk=rand_num)
    return redirect("/{}".format(mineral.name))
