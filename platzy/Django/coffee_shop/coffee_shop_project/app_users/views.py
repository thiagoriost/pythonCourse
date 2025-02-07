# Importa el path para definir rutas y LogoutView para gestionar el logout
from django.urls import path, reverse_lazy
from django.views import generic
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'app_users/register.html'
    success_url = reverse_lazy('login')