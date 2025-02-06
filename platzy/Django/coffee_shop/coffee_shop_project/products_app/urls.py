from django.contrib import admin
from django.urls import path

from products_app.views import PrductFormView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='list_products'),
    path('agregar/', PrductFormView.as_view(), name='add_product'),
]