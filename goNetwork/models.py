from django.db import models

# Create your models here.
class Sede(models.Model):
    COUNTRY = (
        ('CO','Colombia'),
        ('HA','Haiti'),
        ('HO','Honduras'),
        ('PA','Panama'),
        ('PR','Puerto Rico'),
        ('RD','Republica Dominicana'),
        ('US','Estados Unidos'),
    )
    COMPANY = (
        ('CEL','Celsia'),
        ('CEM','Cementos Argos'),
        ('GRP','Grupo Argos'),
        ('CGA','Cementos Argos - Grupo Argos'),
        ('INT','Interejecutiva'),
        ('SAT','Sator'),
        ('SUM','Summa'),
    )
    BUSSINESS = (
        ('AGR','Agregados'),
        ('CEL','Celsia'),
        ('GEM','Cementos'),
        ('CON','Concretos'),
        ('GRP','Grupo Argos'),
        ('LOG','Logitrans'),
        ('SAT','Sator'),
        ('SUM','Summa'),
        ('ZNF','Zona Franca'),
    )
    TYPE = (
        ('ADM','Administrativa'),
        ('PLT','Planta'),
        ('SUB','Subestacion')
    )
    name = models.CharField(max_length=15)
    country = models.CharField(max_length=2, choices=COUNTRY)
    company = models.CharField(max_length=3, choices=COMPANY)
    business = models.CharField(max_length=4, choices=BUSSINESS)    
    type_sede = models.CharField(max_length=4, choices=TYPE)

    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.name, self.type_sede, self.country, self.company, self.business)
    
class Device(models.Model):
    sede = models.ForeignKey(Sede, related_name='devices', on_delete=models.CASCADE)
    site = models.CharField(max_length=15, null=True, blank=True)
    hostname = models.CharField(max_length=15, null=True, blank=True)
    ip_address = models.CharField(max_length=15, null=True, blank=True)
    MAC_address = models.CharField(max_length=15, null=True, blank=True)
    SN = models.CharField(max_length=15, null=True, blank=True)
    brand = models.CharField(max_length=15, null=True, blank=True)
    model = models.CharField(max_length=15, null=True, blank=True)
    type_device = models.CharField(max_length=15, null=True, blank=True)
    subtype_device = models.CharField(max_length=15, null=True, blank=True)
    power_supply = models.CharField(max_length=15, null=True, blank=True)
    power_supply_redundancy = models.BooleanField()
    os = models.CharField(max_length=15, null=True, blank=True)
    version = models.CharField(max_length=15, null=True, blank=True)
    date_update_os = models.DateField()
    telnet = models.BooleanField()
    ssh = models.BooleanField()
    http = models.BooleanField()
    https = models.BooleanField()
    prtg = models.BooleanField()
    orion = models.BooleanField()
    icmp = models.BooleanField()
    snmp = models.CharField(max_length=15, null=True, blank=True)
    snmp_comunity = models.CharField(max_length=15, null=True, blank=True)
    date_install = models.DateField()
    date_end_support = models.DateField()
    date_retired = models.DateField()
    state = models.CharField(max_length=15, null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return '%s %s' % (self.ip_address, self.hostname)
    
