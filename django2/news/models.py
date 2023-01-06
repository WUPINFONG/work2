from django.db import models

# Create your models here.
class News(models.Model):
    title =models.CharField(max_length=50)
    link=models.CharField(max_length=225)
    photo=models.CharField(max_length=255)
    create_date=models.DateField(auto_now_add=True)
    
    class Meta :
        db_table="news"


        