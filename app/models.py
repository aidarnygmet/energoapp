from django.db import models

# Create your models here.
class ugol(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
class mazut(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
class kotel_status(models.Model):
    kotel_id = models.IntegerField()
    kotel_status = models.IntegerField()
    begin = models.DateTimeField()
    end = models.DateTimeField(null=True)
class kotel_info(models.Model):
    kotel_id = models.IntegerField()
    ugol_con = models.FloatField()
    mazut_con = models.FloatField()
    par = models.FloatField()
    temp = models.FloatField()
    pressure = models.FloatField()
    goal_temp = models.FloatField()
    time = models.FloatField()
    parTotal = models.FloatField()
    status = models.IntegerField()
    f1 = models.IntegerField()
    f2 = models.IntegerField()
    f3 = models.IntegerField()
    f4 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
