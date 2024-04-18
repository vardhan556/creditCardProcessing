from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RegistrationDetails(models.Model):
    # user_name=models.CharField(max_length=255)
    user_id=models.CharField(max_length=16,unique=True,primary_key=True)
    password=models.CharField(max_length=255)
    email_id=models.EmailField(max_length=255)
    phone_number=models.IntegerField(max_length=10,unique=True)


class CreditCard(models.Model):
    user_id=models.ForeignKey(RegistrationDetails,on_delete=models.CASCADE,default=None) 
    cardholder_name=models.CharField(max_length=255)
    account_number=models.CharField(max_length=25,unique=True)
    expiration_date=models.CharField(max_length=10)
    cvv=models.CharField(max_length=4,null=True,blank=True)

    def __str__(self):
        return self.cardholder_name

 
# class Vardhan(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()

#     def __str__(self):
#         return self.name

class Product(models.Model):
    user_id=models.ForeignKey(RegistrationDetails,on_delete=models.CASCADE,default=None)
    product_name=models.CharField(max_length=255)
    product_id=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product_name