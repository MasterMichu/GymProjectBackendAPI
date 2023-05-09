from django.db import models
from django.conf import settings

# Create your models here.
class Trainers(models.Model):
    name=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,unique=True)
    methodsdescription=models.CharField(max_length=1000, default="no description provided")

    # add aditional fields in here


class Gymgoer(models.Model):
    name=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,unique=True)
    goaldescription=models.CharField(max_length=1000, default="no description provided")
    # add aditional fields in here


class Gymconnetion(models.Model):
    trainername = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    gymusername = models.ForeignKey(Gymgoer, on_delete=models.CASCADE)
    acceptance = models.BooleanField(default=False)

    def __str__(self):
        return self.trainername