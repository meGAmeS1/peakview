from rest_framework import viewsets
from .models import Peak
from .serializers import PeakSerializer
from rest_framework_gis.filters import InBBoxFilter


class PeakViewSet(viewsets.ModelViewSet):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True
