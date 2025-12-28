from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images')
    title= models.CharField(max_length=10)
    image= models.ImageField(upload_to="gallery")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # agadi pachadi double underlone ho
        return self.title