from django.urls import reverse_lazy
from django.views import generic
from products_app.models import Product
from products_app.forms import ProductForm

class PrductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    template_name = 'products/list_products.html'
    model = Product
    context_object_name = 'products'
    
    # def get_queryset(self):
    #     return Product.objects.all()