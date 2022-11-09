from django.db import models

# Create your models here.
class Zone(models.Model):

    name = models.CharField(max_length=20) 
    def __str__(self):
        return '%s, %s' % (self.id, self.name)

class Business(models.Model):

    name = models.CharField(max_length=20) 
    def __str__(self):
        return '%s, %s' % (self.id, self.name)

class Company(models.Model):

    name = models.CharField(max_length=20)  
    def __str__(self):
        return '%s, %s' % (self.id, self.name)

class Country(models.Model):

    name = models.CharField(max_length=20)
    def __str__(self):
        return '%s, %s' % (self.id, self.name)

class Type_sede(models.Model):

    name = models.CharField(max_length=20)    
    
    def __str__(self):
        return '%s, %s' % (self.id, self.name)

class Sede(models.Model):

    name = models.CharField(max_length=20)
    type_sede = models.ForeignKey(Type_sede, related_name='type_sede', on_delete=models.CASCADE)    
    country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE)  
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)  
    business = models.ForeignKey(Business, related_name='business', on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, related_name='zone', on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s, %s' % (self.id, self.name, self.type_sede, self.zone, self.business, self.company, self.country)
    

    