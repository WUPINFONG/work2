from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import Hotelchange
class HotelAdmin(admin.ModelAdmin):
    list_display=('title','number','content')

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Hotelchange)
