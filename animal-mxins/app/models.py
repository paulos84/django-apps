from django.db import models
from datetime import date


class Person(models.Model):
    name = models.CharField(max_length=50)

class Pet(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Person, on_delete='CASCADE')
    # ......
    born = models.DateTimeField()
    acquired = models.DateTimeField()


class Ownable(models.Model):
    owner = models.ForeignKey(Person, on_delete='CASCADE')

    class Meta:
        abstract = True

class Ageable(models.Model):
    born = models.DateTimeField()
    acquired = models.DateTimeField()

    @property
    def age(self):
        if self.born:
            td = date.today() - self.born
            return td.days/365

    @property
    def owned_for(self):
        return (datetime.now() - self.acquired).days





# from datetime import date
# birthday = date(year=2005, month=11, day=1)


