from django.db import models

# Create your models here.
class Ubication(models.Model):
    country = models.CharField(max_length=15)
    company = models.CharField(max_length=15)
    business = models.CharField(max_length=15)
    sede = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    
