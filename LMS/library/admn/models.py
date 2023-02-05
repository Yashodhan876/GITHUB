from django.db import models

# Create your models here.
class Part_2(models.Model):
    s_no=models.AutoField
    Book_id= models.IntegerField()
    Book_Name= models.CharField(max_length=75,default="")
    author = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.Book_Name

class Part_3(models.Model):
    s_no=models.AutoField
    Book_id= models.IntegerField()
    Book_Name= models.CharField(max_length=75,default="")
    author = models.CharField(max_length=100,default="")
    applicantname= models.CharField(max_length=50,default="None")

    def __str__(self):
        return str(self.Book_Name)+'['+str(self.applicantname)+']'

class Part_4(models.Model):
    s_no=models.AutoField
    Book_id= models.IntegerField()
    Book_Name= models.CharField(max_length=75,default="")
    author = models.CharField(max_length=100,default="")
    applicantname= models.CharField(max_length=50,default="None")
    sactime= models.CharField(max_length=10,default='')
    rettime= models.CharField(max_length=10,default='--')

    def __str__(self):
        return str(self.Book_Name)+'['+str(self.applicantname)+']'