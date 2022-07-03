from django.shortcuts import render
from . models import maps
from django.http import HttpResponse


def index(request):
    allmaps = maps.objects.all()
    print(maps)
    context = {
        'allmaps': allmaps
    }
    return render(request, 'allmaps.html', context=context)


