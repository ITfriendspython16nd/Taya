from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey('Category', related_name='categories')
    