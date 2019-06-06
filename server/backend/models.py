from django.db import models
from django.contrib.auth.models import User

class AmountDetail(models.Model):
    kind = models.CharField(max_length=4)
    amount = models.IntegerField()
    year = models.IntegerField()


class AmountTotal(models.Model):
    kind = models.CharField(max_length=4)
    amount = models.IntegerField()
    year = models.IntegerField()
