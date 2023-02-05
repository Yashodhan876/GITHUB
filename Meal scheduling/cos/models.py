from django.db import models

# Create your models here.
class menu_card(models.Model):
    dish_id=models.AutoField
    dish_name=models.CharField(max_length=50)
    dish_price=models.CharField(max_length=10)
    dish_type=models.CharField(max_length=50)
    image=models.ImageField(upload_to="cos/images",default="")
    def __str__(self):
        return self.dish_name

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(default=' ',max_length=100)
    last_name=models.CharField(default=' ',max_length=100)
    phoneno=models.IntegerField(default=0,max_length=10)
    orderdate=models.CharField(default=' ',max_length=50)
    sheduletime=models.CharField(default=' ',max_length=50)
    dish_list=models.CharField(default=' ',max_length=1000)
    quantity_list=models.CharField(default=' ',max_length=1000)
    price_list=models.CharField(default=' ',max_length=1000)
    members=models.IntegerField(default=0,max_length=2)
    total=models.IntegerField(default=0,max_length=10)
    def __str__(self):
        return str(self.first_name)+str(self.phoneno)