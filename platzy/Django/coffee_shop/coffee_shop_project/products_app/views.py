from django.urls import reverse_lazy  # Importa reverse_lazy para construir URLs de forma perezosa
from django.views import generic  # Importa las vistas genéricas de Django para facilitar la creación de vistas comunes
from products_app.models import Product  # Importa el modelo Product de la aplicación products_app
from products_app.forms import ProductForm  # Importa el formulario ProductForm para gestionar los datos del producto

class PrductFormView(generic.FormView):  # Define la clase PrductFormView, heredando de generic.FormView para manejar formularios
    template_name = 'products/add_product.html'  # Especifica la plantilla que se usará para renderizar el formulario
    form_class = ProductForm  # Indica que se utilizará ProductForm para la validación y manejo de datos
    success_url = reverse_lazy('list_products')  # Define la URL de redirección al enviarse el formulario correctamente

    def form_valid(self, form):  # Método que se ejecuta cuando el formulario enviado es válido
        form.save()  # Guarda el formulario, creando o actualizando una instancia de Product en la base de datos
        return super().form_valid(form)  # Llama al método form_valid de la clase base para gestionar la redirección

class ProductListView(generic.ListView):  # Define la clase ProductListView, heredando de generic.ListView para mostrar una lista de objetos
    template_name = 'products/list_products.html'  # Especifica la plantilla para renderizar la lista de productos
    model = Product  # Indica que la vista se basará en el modelo Product para obtener los datos
    context_object_name = 'products'  # Establece el nombre de la variable de contexto que contendrá la lista de productos en la plantilla

    # def get_queryset(self):
    #     return Product.objects.all()  # Ejemplo de cómo personalizar el queryset; por defecto, ListView obtiene todos los objetos del modelo
