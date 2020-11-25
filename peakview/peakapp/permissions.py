from rest_framework.permissions import BasePermission
from .models import CountryWhiteList, BlockedLog
import logging


logger = logging.getLogger(__name__)


class IpFilteringPermission(BasePermission):
    message = "IP Geolocation not allowed"

    def has_permission(self, request, view):
        try:
            # If there is no whitelist, skip
            if not CountryWhiteList.objects.count():
                return True

            ip_country = request.ipinfo.details.get('country')

            if not ip_country:
                return False

            allowed_countries = [
                country.lower() for country in CountryWhiteList.objects.all().values_list('country', flat=True)
            ]

            if ip_country.lower() in allowed_countries:
                return True

            log = BlockedLog(
                ip=request.ipinfo.details.get('ip'),
                city=request.ipinfo.details.get('city'),
                country=request.ipinfo.details.get('country'),
            )
            log.save()
        except Exception:
            logger.exception("Failed to geolocate IP")

        return False
