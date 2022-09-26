from asyncio.windows_events import NULL
from email.headerregistry import Address
from django.db import models

# Create your models here.

class Patient(models.Model):
  User=(
    ("Patient","Patient"),
    ("Doctor","Doctor")
  )

  user = models.CharField(max_length = 20,choices = User)
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  profile_picture=models.ImageField(upload_to='files/',null=True,blank=True)
  username=models.CharField(max_length=50,unique=True)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=50)
  confirm_password=models.CharField(max_length=50)
  address1 = models.CharField("Address line 1", max_length=100,)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  pincode = models.CharField(max_length=12)


class Doctor(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  profile_picture=models.ImageField(upload_to='files/',null=True,blank=True)
  username=models.CharField(max_length=50,unique=True)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=50)
  confirm_password=models.CharField(max_length=50)
  address1 = models.CharField("Address line 1", max_length=100,)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  pincode = models.CharField(max_length=12)
