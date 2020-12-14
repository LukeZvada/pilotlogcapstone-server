"""New Flight Log model module"""
from django.db import models


class NewLog(models.Model):
    """NewLog database model"""
    user_id = models.ForeignKey("AircraftProfile", on_delete=models.CASCADE)
    aircraftprofileId = models.ForeignKey("AircraftProfile", on_delete=models.CASCADE)
    date = models.DateField(default="0000-00-00",)
    make_and_model = models.CharField(max_length=50)
    aircraftId = models.CharField(max_length=25)
    fromAiport = models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    landingsDay = models.IntegerField()
    landingsNight = models.IntegerField()
    number_of_instrument_approaches = models.IntegerField()
    type_and_location = models.CharField(max_length=50)
    airplane_single_multi = models.BooleanField(default=True,)
    airplane_single_multi_hours = models.IntegerField()
    intrumentActual = models.IntegerField()
    simulator_hood = models.IntegerField()
    ftd_or_simulator = models.IntegerField()
    night = models.IntegerField()
    cross_country_all = models.IntegerField()
    cross_country_fivezero = models.IntegerField()
    pilot_in_command = models.IntegerField()
    solo = models.IntegerField()
    ground_training = models.IntegerField()
    flight_training_received = models.IntegerField()
    flight_training_given = models.IntegerField()
    total_flight_time = models.IntegerField()