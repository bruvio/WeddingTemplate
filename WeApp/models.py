from django.db import models
attend_choices = (
        ('yes', 'Yes, I will be attending'),
        ('no', 'No, I will not be attending'),
    )

# Create your models here.
class RSVP(models.Model):
    name = models.CharField( max_length=255, null=True)
    phone = models.CharField( max_length=11, null=True)
    attend = models.CharField(max_length=3, choices=attend_choices, null=False)
    

class Comments(models.Model):
    name = models.CharField( max_length=500, null=True)
    question = models.CharField( max_length=500, null=True)
    Answer = models.CharField( max_length=500, null=True)

class Hotels(models.Model):
    H_name = models.CharField( max_length=50, null=True)
    H_Desc = models.CharField( max_length=20, null=True)
    H_Price = models.CharField( max_length=20, null=True)
    H_link = models.CharField( max_length=20, null=True)

class Excurisons(models.Model):
    E_name = models.CharField( max_length=50, null=True)
    E_Desc = models.CharField( max_length=20, null=True)
    E_Price = models.CharField( max_length=20, null=False)
    E_link = models.CharField( max_length=20, null=True)


class Flights(models.Model):
    F_name = models.CharField( max_length=50, null=True)
    F_Desc = models.CharField( max_length=20, null=True)
    F_Price = models.CharField( max_length=20, null=True)
    F_link = models.CharField( max_length=20, null=True)
