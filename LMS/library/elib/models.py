from django.db import models
import os

# Create your models here.
class Book(models.Model):
    s_no=models.AutoField
    Book_id= models.IntegerField()
    Book_Name= models.CharField(max_length=75,default="")
    author = models.CharField(max_length=100,default="")
    category = models.CharField(max_length=30,default="")
    ISBN_10 = models.CharField(max_length=12,default="")
    desc= models.CharField(max_length=100,default="")
    image= models.ImageField(upload_to="elib/images",default="")
    pdf= models.FileField(upload_to="elib/pdf",default="elib/pdf/Soft_Copy_of_Book_is_Not_Available.pdf")

    def __str__(self):
        return self.Book_Name
    
    