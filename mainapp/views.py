from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mainapp.forms import AddPlantForm, CreateUserForm, UserLoginForm, AddImageForm
from mainapp.models import Category, Plant, Image


def plant_list(request):
    plants = Plant.objects.all()
    images = Image.objects.all()
    plants_list = []
    images_list = []
    for item in plants:
        plants_list.append(item)
        images_list.append(list(images.filter(plant_id=item.pk))[0])
    return render(request, 'mainapp/plant_list_view.html', {'plants': zip(plants_list, images_list)})


def plant_detail(request, plant_pk):
    plant = Plant.objects.get(id=plant_pk)
    images = Image.objects.filter(plant_id=plant_pk)
    if len(images) <= 3:
        height = 380
    elif len(images) <= 6:
        height = 700
    else:
        height = 1030
    return render(request, 'mainapp/plant_detail_view.html', {'one_plant': plant, 'images':images, 'height':height})



def add_plant(request):
    if request.method == 'POST':
        plant_form = AddPlantForm(request.POST)
        image_form = AddImageForm(request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            plant_id = Plant.objects.get(title=request.POST['title'])
            for img in request.FILES.getlist('attachments'):
                Image.objects.create(image=img,plant_id=plant_id.pk)
            return redirect('plant_list_view')
    else:
        plant_form = AddPlantForm()
        image_form = AddImageForm()
    context = {'form': [plant_form, image_form]}

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