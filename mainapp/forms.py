from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from multiupload.fields import MultiImageField
from mainapp.models import Plant, Image


class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plant

        fields = ('category', 'title', 'place_of_purchase', 'price', 'date_of_purchase', 'date_of_plant',
    'date_of_collect', 'date_of_last_water', 'description')


class AddImageForm(forms.Form):
    attachments = MultiImageField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 5)




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


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(
        attrs={"placeholder": "Введите имя пользователя"}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}))