from django.db import models

# Create your models here.

lapcompanyname_choices = (
    ('Asus','Asus'),
    ('Hp','HP'),
    ('Lenovo','Lenovo'),
    ('Dell','Dell')
)

class Laptop(models.Model):
   lapmodelname = models.CharField(max_length=30)
   lapcompanyname = models.CharField(max_length=30,choices=lapcompanyname_choices)
   ram = models.IntegerField()
   rom = models.IntegerField()
   weight = models.FloatField()
   processor = models.CharField(max_length=30)
   is_paid = models.BooleanField()
