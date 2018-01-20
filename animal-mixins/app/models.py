from django.db import models
from datetime import date
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
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)
    # born = models.DateTimeField()




# from datetime import date
# birthday = date(year=2005, month=11, day=1)


