import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Smog(models.Model):
    name = models.CharField(max_length=300)
    note = models.CharField(max_length=3000)
    parcel = models.CharField(max_length=300)
    lv = models.CharField(max_length=300)
    legality_status = models.CharField(max_length=300)
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    cadaster = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
