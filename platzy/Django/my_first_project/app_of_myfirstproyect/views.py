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
