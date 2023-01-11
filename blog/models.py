from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogs/images')
    URLField=models.URLField(blank=True)


    