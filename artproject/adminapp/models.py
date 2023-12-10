from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#Admin table
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "admin_table"
#Artist Table


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100,blank=False,default="artist123")
    gender_choices = (("MALE", "Male"), ("FEMALE", "Female"), (("Others", "OTHERS")))
    gender = models.CharField(max_length=20, blank=False, default="",choices=gender_choices)
    email = models.EmailField(default="",max_length=100,blank=False)
    category_choices = (("Painter", "Painter"), ("Sculptur", "Sculpture"))
    category = models.CharField(max_length=25,choices=category_choices)
    phonenumber1= models.CharField(max_length=20,blank=False,default="",unique=True)
    address = models.CharField(max_length=100,blank=False,default="")
    artistimage = models.ImageField(upload_to='uploads/',null=True,blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "artist_table"


#Customer Table
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False)
    password = models.CharField(max_length=100, blank=False,default="")
    gender_choices = (("MALE", "Male"), ("FEMALE", "Female"), (("Others", "OTHERS")))
    gender = models.CharField(max_length=20, blank=False, default="",choices=gender_choices)
    phonenumber = models.CharField(max_length=20,blank=False,default="",unique=True)
    email = models.EmailField(default="",max_length=100,blank=False)
    address = models.CharField(max_length=100,blank=False,default="customer123")
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table="customer_table"



class Category(models.Model):
    name_choices = (("OilPaintings", "OilPaintings"), ("PencilPaintings", "PencilPaintings"),("Glasspaintings", "Glasspaintings"),("WaterPaintings", "WaterPaintings"),("CarvedSculptures", "CarvedSculptures"),("AssembledSculptures", "AssembledSculptures"),("ReliefSculptures", "ReliefSculptures"),("ModeledSculptures","ModeledSculptures"))
    name = models.CharField(max_length=100,choices=name_choices)

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Specify the max_digits and decimal_places
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # Assuming you have a Category model
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/',null=True,blank=True)

    def __str__(self):
        return self.name
#class Profile(models.Model):
 #   user= models.OneToOneField(User,on_delete=models.CASCADE)
  #  email_token=models.CharField(max_length=200)
   # is_verified=models.BooleanField(default=False)

