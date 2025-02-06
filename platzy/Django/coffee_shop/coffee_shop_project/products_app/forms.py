


from django import forms

from products_app.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=200)
    description = forms.CharField(label='Descripción', max_length=300)
    price = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)
    available = forms.BooleanField(label='Disponible', required=False, initial=True)
    photo = forms.ImageField(label='Foto', required=False)
    # date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación', null=True)
    date = forms.DateTimeField(label='Fecha de creación', required=False)
    
    def save(self):
        data = self.cleaned_data
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            date=data['date'],
            photo=data['photo']
        )
        return product