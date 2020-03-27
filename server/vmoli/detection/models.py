from django.db import models

# Create your models here.
class Test(models.Model):
	nickname = models.CharField(max_length=20)



class ImageModel(models.Model):
	image = models.ImageField(upload_to="image/%Y/%m/%d", blank=True)