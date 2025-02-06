from django.contrib import admin

from products_app.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'description', 'price', 'available', 'photo', 'date']
    search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)