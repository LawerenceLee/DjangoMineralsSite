from django.shortcuts import render


from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'catalog/index.html', {"minerals": minerals})
