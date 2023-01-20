from django.db import models

# Create your models here.
class DealsOfTheDay(models.Model):
    prod_id=models.AutoField
    prod_name=models.CharField(max_length=50,default='')
    prod_desc=models.CharField(max_length=100,default='')
    prod_price=models.IntegerField()
    image = models.ImageField(upload_to='app/images',default='')


    def __str__(self):
        return self.prod_name