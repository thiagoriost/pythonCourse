from typing import Any
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view(request):
    
    car_list = [
        {"title": "BMW"},
        {"title": "MAZDA"},
    ]
    
    context = {
        "car_list": car_list
    }
    return render(request, 'app_of_myfirstproyect\car_list.html', context=context)

class CarListView(TemplateView):
    print("CarListView => ----")
    template_name = 'app_of_myfirstproyect\car_list.html'
    
    def get_context_data(self, **kwargs):
        
        car_list = [
            {"title": "BMW"},
            {"title": "MAZDA"},
            {"title": "Chevrolet"},
        ]
        
        return {
            "car_list": car_list
        }
    

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

