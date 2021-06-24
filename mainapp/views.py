from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from mainapp.models import Category, Plant


class PlantListView(ListView):
    model = Plant
    template_name = 'mainapp/plant_list_view.html'
    context_object_name = 'plants'

    # выбираю только темы, относящиеся к конкретной категории
    def get_queryset(self):
        return Plant.objects.all()
