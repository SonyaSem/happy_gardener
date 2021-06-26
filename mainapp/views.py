from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mainapp.forms import AddPlantForm, CreateUserForm, UserLoginForm
from mainapp.models import Category, Plant, Photo


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
        # images will be in request.FILES
        form = AddPlantForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            place_of_purchase = form.cleaned_data['place_of_purchase']
            date_of_purchase = form.cleaned_data['date_of_purchase']
            price = form.cleaned_data['price']
            date_of_plant = form.cleaned_data['date_of_plant']
            date_of_collect = form.cleaned_data['date_of_collect']
            date_of_last_water = form.cleaned_data['date_of_last_water']

            plant_obj = Plant.objects.create(title=title,
                                             category=category, description=description,
                                             place_of_purchase=place_of_purchase,
                                             date_of_purchase=date_of_purchase, price=price,
                                             date_of_plant=date_of_plant,
                                             date_of_collect=date_of_collect, date_of_last_water=date_of_last_water)
            for file in files:
                Photo.objects.create(plant=plant_obj, image=file)

        else:
            print("Form invalid")

    else:
        form = AddPlantForm()
    context = {'form': form}

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