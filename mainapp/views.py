from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.http import HttpResponse

from mainapp.forms import AddPlantForm, CreateUserForm, UserLoginForm
from mainapp.models import Category, Plant
from . import ShareService


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
        plant_form = AddPlantForm(request.POST, request.FILES)
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


class Insta_share_choice(DetailView):
    model = Plant
    template_name = 'mainapp/Instagram_preshare.html'
    context_object_name = 'one_plant'


def instagram_share_preview(request):
    if request.method == 'POST':
        choosen_data_for_post = request.POST.getlist('check')
        final_text = ''.join(choosen_data_for_post)
        if len(final_text) > ShareService.INSTAGRAM_MAX_CAPTION_SIMBOLS_AMOUNT:
            messages.error(request, "Внимание, количество символов описания было превышено на " +
                           str(len(final_text) - ShareService.INSTAGRAM_MAX_CAPTION_SIMBOLS_AMOUNT) + " символов")
        if 'images' not in request.POST:
            messages.error(request, "Внимание, ни одна фотография не была выбрана!")
            images = []
        else:
            images = request.POST.getlist('images')
            if len(images) > ShareService.INSTAGRAM_MAX_PICTURE_AMOUNT:
                messages.error(request, "Внимание, число фото в одном посте не может быть больше: " +
                               str(ShareService.INSTAGRAM_MAX_PICTURE_AMOUNT))
    return render(request, 'mainapp/Insta_Post_preview.html', {'text': final_text,
                                                               'images': images})


def post_to_insta(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        images = request.POST.getlist('picture')
        login = request.POST.get('login')
        password = request.POST.get('password')
        for index, image in enumerate(images):
            images[index] = '.' + images[index]
        print(login, password, images, caption)
        ShareService.share_to_instagram(login, password, images, caption)
        messages.success(request, "Пост был успешно отправлен в инстграм")
    return HttpResponse("Всё ок")
