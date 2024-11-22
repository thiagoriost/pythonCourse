from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
        {"marca": "BMW"},
        {"marca": "Mazda"},
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_template_app/car_list.html", context)