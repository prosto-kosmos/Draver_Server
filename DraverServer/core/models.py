from django.db import models

class Drivers(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=40)
    firstname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)

class Logs(models.Model):
    log_id = models.IntegerField(primary_key=True, auto_created=True)
    driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    speed = models.CharField(max_length=10)
    rpm = models.CharField(max_length=15)
