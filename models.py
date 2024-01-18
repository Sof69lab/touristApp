from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    name = models.TextField()
    route = models.TextField()
    duration = models.FloatField()
    days = models.IntegerField(blank=True)
    describe = models.TextField()
    photo = models.ImageField(upload_to='images', blank=True)
    transport = models.TextField()
    price = models.FloatField()

class Reservation(models.Model):
    name = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    people = models.IntegerField()
    cost = models.FloatField()
