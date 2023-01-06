from django.contrib import admin

# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','create_data')

admin.site.register(Product,ProductAdmin)