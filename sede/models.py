from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=20)

class Company(models.Model):
    name=models.CharField(max_length=20)

class Busines(models.Model):
    name=models.CharField(max_length=20)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE)

    def __str__(self):
        return '%s_%s_%s' % (self.name, self.company, self.country)

class Type(models.Model):
    name=models.CharField(max_length=20)

class Sede(models.Model):
    
    name=models.CharField(max_length=20)
    type=models.ForeignKey(Type, related_name='type', on_delete=models.CASCADE)
    busines=models.ForeignKey(Busines, related_name='busines', on_delete=models.CASCADE)