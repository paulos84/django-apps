from django.db import models
from datetime import date, datetime
from django.utils import timezone


class Timestampable(models.Model):
    var = models.CharField(max_length=40)
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


class Ageable(models.Model):
    born = models.DateTimeField()

    class Meta:
        abstract = True

    @property
    def age(self):
        if self.born:
            td = date.today() - self.born
            return td.days/365
