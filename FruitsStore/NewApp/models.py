from django.db import models

# Create your models here.
class catdata(models.Model):
    cat_name = models.CharField(max_length=100, null=True, blank=True)
    cat_dec = models.CharField(max_length=100, null=True, blank=True)
    cat_quan = models.CharField(max_length=100, null=True, blank=True)
    cat_price = models.IntegerField(null=True, blank=True)
    images = models.ImageField(upload_to='cate', null=True, blank=True)


class catdetail(models.Model):
    cate_nam = models.CharField(max_length=100, null=True, blank=True)
    cate_de = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='cat', null=True, blank=True)