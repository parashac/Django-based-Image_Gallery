from django.db import models

# Create your models here.
class Image(models.Model):
    title= models.CharField(max_length=100)
    image= models.ImageField(upload_to="gallery/")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # agadi pachadi double underline ho
        return self.title