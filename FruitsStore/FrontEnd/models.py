from django.db import models

# Create your models here.
class logindb(models.Model):
    s_name = models.CharField(max_length=100, null=True, blank=True)
    s_user = models.CharField(max_length=100, null=True, blank=True)
    s_pass = models.CharField(max_length=100, null=True, blank=True)



class contactdb(models.Model):
    c_name = models.CharField(max_length=100, null=True, blank=True)
    c_email = models.CharField(max_length=100, null=True, blank=True)
    c_subject = models.CharField(max_length=100, null=True, blank=True)
    c_message = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):

    ca_name = models.CharField(max_length=100, null=True, blank=True)
    ca_price = models.CharField(max_length=100, null=True,blank=True)
    ca_qty = models.CharField(max_length=100, null=True, blank=True)
    ca_total = models.CharField(max_length=100, null=True, blank=True)