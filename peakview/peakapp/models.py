from django.contrib.gis.db import models
from django.core import validators
from django_countries.fields import CountryField


# Create your models here.
class Peak(models.Model):
    location = models.PointField(null=False, blank=False)
    elevation = models.FloatField(null=False, blank=False, validators=[validators.MinValueValidator(0)])
    name = models.CharField(max_length=128, null=False, blank=False)


class CountryWhiteList(models.Model):
    country = CountryField()


class BlockedLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=128, blank=False, null=False)
    city = models.CharField(max_length=128, blank=False, null=False)
    country = models.CharField(max_length=128, blank=False, null=False)
