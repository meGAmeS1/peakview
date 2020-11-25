from django.contrib import admin
from .models import Peak, CountryWhiteList, BlockedLog
from django.contrib.gis.admin import GeoModelAdmin


@admin.register(Peak)
class PeakAdmin(GeoModelAdmin):
    default_zoom = 4
    list_display = ('name', )


@admin.register(CountryWhiteList)
class CountryWhiteListAdmin(admin.ModelAdmin):
    list_display = ('country', )


@admin.register(BlockedLog)
class BlockedLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'ip', 'city', 'country', )
