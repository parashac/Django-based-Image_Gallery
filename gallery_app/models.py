from django.db import models

# Create your models here.
class Image(models.Model):
    title= models.CharField(max_length=10)
    image= models.ImageField(upload_to ="/gallery")

    def __str__(self):  # agadi pachadi double underlone ho
        return self.title