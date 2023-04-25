from django.db import models
from django.contrib.postgres.fields import ArrayField

class Monitored(models.Model):
  tickers = ArrayField(models.TextField())

  def __str__(self):
    return self.tickers