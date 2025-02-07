urlpatterns = [
    path('', ProductListView.as_view(), name='list_products'),
    path('agregar/', PrductFormView.as_view(), name='add_product'),
]