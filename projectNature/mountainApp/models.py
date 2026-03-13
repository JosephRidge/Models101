from django.db import models

# Create your models here.
class HikeEvent(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=150)
    arrival_time =models.TimeField()
    image_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mountain(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()
    isVolcanic = models.BooleanField(default=False)
    image_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

