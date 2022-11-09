from django.db import models

# Create your models here.
class Sede(models.Model):

    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    business = models.CharField(max_length=20)   
    type_sede = models.CharField(max_length=20)

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
    
