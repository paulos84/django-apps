from django.db import models
from datetime import date
from django.utils import timezone


class Ageable(models.Model):
    born = models.DateTimeField()

    class Meta:
        abstract = True

    @property
    def age(self):
        if self.born:
            td = date.today() - self.born
            return td.days/365


class Timestampable(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Timestampable, self).save(*args, **kwargs)


