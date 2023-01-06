from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    photo_url=models.CharField(max_length=255)
    product_url=models.CharField(max_length=255)
    discount=models.FloatField()
    create_data=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table='product'
        
    