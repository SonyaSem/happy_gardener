from django.urls import path

from mainapp.views import PlantListView, PlantDetailView, add_plant

urlpatterns = [
    path('plant_list/', PlantListView.as_view(), name='plant_list_view'),
    path('plant_detail/<int:pk>', PlantDetailView.as_view(), name='plant_detail_view'),
    path('add_plant/', add_plant, name='add_plant'),

    ]