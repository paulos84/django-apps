from .models import AnnualMean, DailyMean
from rest_framework import serializers


class AnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualMean
        fields = ('Site', 'Year', 'Pollutant', 'Concentration')

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMean
        fields = ('Site', 'Date', 'Pollutant', 'Concentration')

