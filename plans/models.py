from django.db import models
from django.conf import settings
from django.core.validators import ValidationError

# Create your models here.
class LowerField(models.CharField):
    def get_prep_value(self,value):
        return str(value).lower()

class PlanName(models.Model):
    name=LowerField(max_length=50)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Plans(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,unique=False)
    excercise=models.ForeignKey("AvilableExcercises",on_delete=models.CASCADE,unique=False)
    planname=models.ForeignKey(PlanName,on_delete=models.CASCADE,unique=False)


class AvilableExcercises(models.Model):
    name=LowerField(max_length=50)
    musclesgroup=models.ForeignKey('musclesgroup',on_delete=models.CASCADE,unique=False)
    image = models.ImageField(null=False, blank=False, upload_to="./images", unique=True)
    description= models.CharField(max_length=3000)

    def __str__(self):
        return self.name
class Musclesgroup(models.Model):
    name=LowerField(max_length=50)
    image = models.ImageField(null=False, blank=False, upload_to="./images", unique=True)
    def __str__(self):
        return self.name

class Traninglog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.Model, unique=False)
    excercise = models.ForeignKey("AvilableExcercises",on_delete=models.CASCADE, unique=False)
    reps = models.IntegerField()
    weight = models.FloatField()
    date = models.DateField()