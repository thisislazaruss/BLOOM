from django.db import models

class image_upload(models.Model):
    image_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    


