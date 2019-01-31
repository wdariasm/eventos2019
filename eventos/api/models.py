from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=50)

class Events(models.Model):
    name = models.CharField(max_length=50)
    category  =  models.CharField(max_length=50)
    place = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    modality = models.CharField(max_length=20)
    userId = models.IntegerField()

