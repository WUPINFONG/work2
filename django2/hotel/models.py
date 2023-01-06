from django.db import models

# Create your models here.

class Hotel(models.Model):
    title =models.CharField(max_length=50)
    link=models.CharField(max_length=225)
    photo=models.CharField(max_length=255)
    content=models.TextField()
    number=models.FloatField()
    create_date=models.DateField(auto_now_add=True)
    
    class Meta :
        db_table="hotle"

class Hotelchange(models.Model):
    
    city=models.CharField(max_length=50)
    
    class Meta:
        db_table='city'
        