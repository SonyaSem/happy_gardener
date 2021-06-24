from django.urls import path

from mainapp.views import PlantListView

urlpatterns = [
    path('plant_list/', PlantListView.as_view(), name='plant_list_view'),

    ]