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


def searchamap(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query == 'None'

        resultmap = maps.objects.filter(map_title__icontains=query)

    return render(request, 'search.html', {'resultmap': resultmap})


