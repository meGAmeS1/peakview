from django.contrib import admin
from .models import Peak
from django.contrib.gis.admin import GeoModelAdmin

@admin.register(Peak)
class PeakAdmin(GeoModelAdmin):
    default_zoom = 4
