from django.db import models

# Create your models here.
class Image(models.Model):
    title= models.CharField(max_length=10)
    album=models.ImageField(uploadto_='/gallery/album')
    image= models.ImageField(uploadto_="/gallery")

