from django.db import models
from .mixins import Timestampable, Ageable


class Person(models.Model):
    name = models.CharField(max_length=50)


class Ownable(models.Model):
    owner = models.ForeignKey(Person, on_delete='CASCADE')

    class Meta:
        abstract = True


class Pet(Ownable, Timestampable, Ageable, models.Model):
    # owner = models.ForeignKey(Person, on_delete='CASCADE')
    name = models.CharField(max_length=50)
    diet = models.CharField(blank=True, max_length=50)

