from django.contrib.gis.db import models
from django.core import validators


# Create your models here.
class Peak(models.Model):
    location = models.PointField(null=False, blank=False)
    elevation = models.FloatField(null=False, blank=False, validators=[validators.MinValueValidator(0)])
    name = models.CharField(max_length=128, null=False, blank=False)
