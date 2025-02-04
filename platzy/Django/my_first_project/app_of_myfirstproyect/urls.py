"""
URL configuration for my_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponse


def car_view(request, *args, **kwargs):
    print("args => ", args)
    print("kwargs => ", kwargs)
    return HttpResponse("Listado de carros")

def car_overview_view(request, *args, **kwargs):
    # Filtra los kwargs con valor no None
    valid_kwargs = {key: value for key, value in kwargs.items() if value is not None}
    
    print("Valores válidos en kwargs:", valid_kwargs)
    
    # Construye una cadena con los valores filtrados
    response_values = " ".join(str(value) for value in valid_kwargs.values())
    print("response_values => ", response_values)
    
    # Opcional: también puedes ver el diccionario filtrado en la consola
    
    # Retorna la respuesta HTTP
    return HttpResponse(f"car_overview_view {response_values}")

urlpatterns = [
    path('listado/',car_view),
    path('listado/<int:id>',car_view),
    path('detalle/<int:id>',car_overview_view),
    path('marcas/<str:brand>',car_overview_view),
    path('marcas/<int:id>',car_overview_view)
]
