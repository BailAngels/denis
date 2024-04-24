from django.urls import path

from apps.users.views import sing_up, login


urlpatterns = [
    path('registration/', sing_up, name='registration'),
    path('login/', login, name='login'),
]
