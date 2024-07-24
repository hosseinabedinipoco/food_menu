from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/", null=False)
