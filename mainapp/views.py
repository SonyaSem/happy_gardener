import math
from datetime import date, timedelta, datetime

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mainapp.forms import AddPlantForm, CreateUserForm, UserLoginForm
from mainapp.models import Category, Plant


class PlantListView(ListView):

    def get(self, request, *args, **kwargs):
        for plant in Plant.objects.all():
            current_plant = Plant.objects.get(pk=plant.pk)
            current_date = date.today()
            days_from_plant = current_date - current_plant.date_of_plant
            intervals_to_next_water = days_from_plant.days / plant.interval_of_water
            days_to_next_water = timedelta(days=math.ceil(intervals_to_next_water) * plant.interval_of_water)
            days_to_previous_water = timedelta(days=math.floor(intervals_to_next_water) * plant.interval_of_water)
            Plant.objects.filter(pk=plant.pk).update(
                date_of_last_water=current_plant.date_of_plant + days_to_previous_water)
            Plant.objects.filter(pk=plant.pk).update(
                date_of_upcoming_water=current_plant.date_of_plant + days_to_next_water)

        return super(PlantListView, self).get(request, *args, **kwargs)

    model = Plant
    template_name = 'mainapp/plant_list_view.html'
    context_object_name = 'plants'

    def get_queryset(self):
        return Plant.objects.all()


class PlantDetailView(ListView):
    model = Plant
    template_name = 'mainapp/plant_detail_view.html'
    context_object_name = 'one_plant'

    def get_queryset(self):
        return Plant.objects.get(pk=self.kwargs['pk'])


def add_plant(request):
    if request.method == 'POST':
        plant_form = AddPlantForm(request.POST)
        if plant_form.is_valid():
            plant_form.save()
    else:
        plant_form = AddPlantForm()
    context = {'form': plant_form}

    return render(request, 'mainapp/add_plant.html', context)


class RegisterUserView(CreateView, SuccessMessageMixin):
    model = User
    template_name = "mainapp/register.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('plant_list_view')
    success_message = "Вы успешно зарегистрировались!"


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "mainapp/login.html"


def user_logout(request):
    logout(request)
    return redirect('plant_list_view')
