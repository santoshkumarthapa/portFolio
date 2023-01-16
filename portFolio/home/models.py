from django.db import models

# Create your models here.

class myBackGround(models.Model):
    TAS = models.CharField(max_length=50)
    tas_eno = models.IntegerField()
    tas_sal = models.FloatField()
    tas_res = models.CharField(max_length=250)

