from django.db import models

# Create your models here.

from django.contrib.auth.models import  User

class donor_details(models.Model):

    user =  models.OneToOneField(to = User , on_delete=models.CASCADE , null=True)
    email_status = models.BooleanField(default = False ,blank=False)
    phone  = models.TextField(max_length=15)
    points = models.IntegerField()



class institution_details(models.Model ):

    user =  models.OneToOneField(to = User , on_delete=models.CASCADE , null=True)
    email_status = models.BooleanField(default=False, blank=False)
    phone = models.TextField(max_length=15)
    email_status = models.BooleanField(default=False, blank=False)
    account_holder = models.TextField(max_length=100)
    account_number = models.TextField(max_length=200)
    ifsc = models.TextField(max_length=20)


class post(models.Model ):

    user = models.TextField(max_length=100 , null=True )
    title = models.TextField(max_length=1000)
    body = models.TextField(max_length=2000)
    is_satisfied = models.BooleanField(default=False )

