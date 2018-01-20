from django.db import models
from datetime import date


class Timestampable(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ageable(models.Model):
    born = models.DateTimeField()

    class Meta:
        abstract = True

    @property
    def age(self):
        if self.born:
            td = date.today() - self.born
            return td.days/365
