from django.shortcuts import render

from .models import Places
from links.models import Links
# Create your views here.

def all_places_view(request):
    obj = Places.objects.all()
    data = {
        "object": obj
    }
    return render(request, 'allplaces.html', data)
