from .models import Monitored
from rest_framework import serializers

class MonitoredSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Monitored
    fields = ['url', 'tickers']