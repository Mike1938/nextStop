from django.shortcuts import render

from .models import Places
# Create your views here.

def all_places_view(request):

    return render(request, 'allplaces.html', {})
