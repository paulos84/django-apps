from django.db import models


class AnnualMean(models.Model):
    Site = models.CharField(max_length=50)
    Year = models.IntegerField()
    Pollutant = models.CharField(max_length=30)
    Concentration = models.FloatField(max_length=20)
    url = models.CharField(max_length=50, default='')
    image = models.ImageField(default='')
    aqi = models.CharField(max_length=500,default='')
    poll = models.CharField(max_length=50, default='')

    
class DailyMean(models.Model):
    Site = models.CharField(max_length=50)
    Date = models.DateField(null=True)
    Pollutant = models.CharField(max_length=10)
    Concentration = models.FloatField(max_length=10, null=True)
    url = models.CharField(max_length=50, default='')
    poll = models.CharField(max_length=50, default='')
