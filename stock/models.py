from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Ashokley(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

class Sensex(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

class Cipla(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

class Nifty(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

class Reliance(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

class Tatasteel(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

class Eichermotors(models.Model):
    Open = models.FloatField(blank = False)
    High = models.FloatField(blank = False)
    Low = models.FloatField(blank = False)
    Close = models.FloatField(blank = False)
    Adj_close = models.FloatField(blank = False)
    Volume = models.FloatField(blank = False)
    Date = models.DateTimeField()

