from django.db import models
from django.urls import reverse
import requests
from requests_oauthlib import OAuth1
import csv


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country_detail', args=[str(self.id)])

    @staticmethod
    def populate():
        with open('assignment/countries.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0]:
                    try:
                        obj = Country.objects.get(name=row[0], code=row[1], longitude=row[2], latitude=row[3])
                    except Country.DoesNotExist:
                        obj = Country(name=row[0], code=row[1], longitude=row[2], latitude=row[3])
                        obj.save()


class Tweet(models.Model):
    created_at = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    url = models.URLField(max_length=200)
    countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return 'Tweet made at {}'.format(self.created_at)

    @staticmethod
    def get_tweets():
        url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        auth = OAuth1('M72BiZ9828A9ERCIwAZxaDLkJ', '94Tpp7CYXlCbyTBMSQj2aE399Hvvbe51UdQVuZWwD9vlBgcaeB',
                      '949738713399070720-UGUwHUu7C2PxtrK1sAFh5e8XvM4QU4d',
                      'i2dcngnHbUw58bwDGplWoEzFGaWfsxKP2TpOOdyqxOMNV')
        resp = requests.get(
            'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=MaplecroftRisk&count=50', auth=auth)
        country_list = []
        with open('assignment/countries.csv') as f:
            reader = csv.reader(f)
            for a in reader:
                if a and a[0]:
                    country_list.append(a[0])
        for a in resp.json():
                try:
                    obj = Tweet.objects.get(created_at=a['created_at'], text=a['text'],
                                            url='https://twitter.com/MaplecroftRisk/status/{}'.format(a['id_str']))
                except Tweet.DoesNotExist:
                    obj = Tweet(created_at=a['created_at'], text=a['text'],
                                url='https://twitter.com/MaplecroftRisk/status/{}'.format(a['id_str']))
                    obj.save()
                    country_instances = []
                    for b in country_list:
                        if b in obj.text:
                            country_instances.append(Country.objects.get(name=b))
                            obj.countries.add(*country_instances)

