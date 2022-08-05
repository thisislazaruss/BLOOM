from django.db import models
class breastcancer(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
# Create your models here.
