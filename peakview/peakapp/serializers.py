from rest_framework import serializers
from peakapp import models


class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Peak
        fields = ['url', 'name', 'location', 'elevation']
