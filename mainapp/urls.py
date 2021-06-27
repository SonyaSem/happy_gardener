from django.contrib.auth.views import LoginView
from django.urls import path


from mainapp.views import plant_list, plant_detail, add_plant, RegisterUserView, UserLoginView, user_logout

urlpatterns = [
    path('', plant_list, name='plant_list_view'),
    path('plant_detail/<int:plant_pk>', plant_detail, name='plant_detail'),
    path('add_plant/', add_plant, name='add_plant'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),

    ]

