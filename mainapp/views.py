from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mainapp.forms import AddPlantForm, CreateUserForm
from mainapp.models import Category, Plant


class PlantListView(ListView):
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


# регистрация пользователей
class RegisterUserView(CreateView, SuccessMessageMixin):
    model = User
    template_name = "mainapp/register.html"
    form_class = CreateUserForm
    # my_super_categories - имя маршрута из urls для перехода после успешной регистрации
    success_url = reverse_lazy('plant_list_view')

    # вывод сообщения об успешной регистрации в Index.html
    success_message = "Вы успешно зарегистрировались!"