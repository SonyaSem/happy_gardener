from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mainapp.models import Plant


class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('category', 'title', 'description', 'place_of_purchase', 'price',)


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя")
    email = forms.EmailField(label="Электронная почта")
    password1 = forms.CharField(label="Введите пароль")
    password2 = forms.CharField(label="Повторите пароль")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    error_messages = {
        'password_mismatch': ('Введенные пароли не совпадают'),
    }