"""Aircraft Profile model module"""
from django.db import models


class AircraftProfile(models.Model):
    aircraft_img = models.ImageField()
    aircraft_make_and_model = models.CharField(max_length=50)
    aircraft_color = models.CharField(max_length=50)
    home_airport = models.CharField(max_length=50)
    basic_empty_weight = models.IntegerField()
    max_zero_fuel_weight = models.IntegerField()
    max_takeoff_weight = models.IntegerField()
    ident_number = models.CharField(max_length=50)
    altitude = models.IntegerField()
    cruise_speed = models.IntegerField()