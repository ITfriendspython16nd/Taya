from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',null=True)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=225)