"""New Flight Log model module"""
from pilotlogapi.models.pilotlogusers import PilotLogUsers
from django.db import models


class NewLog(models.Model):
    """NewLog database model"""
    PilotLogUserId = models.ForeignKey(PilotLogUsers, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    make_and_model = models.CharField(max_length=50)
    aircraftId = models.CharField(max_length=25)
    fromAirport = models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    landingsDay = models.IntegerField()
    landingsNight = models.IntegerField()
    number_of_instrument_approaches = models.IntegerField()
    type_and_location = models.CharField(max_length=50)
    airplane_single_multi = models.BooleanField(default=True,)
    airplane_single_multi_hours = models.IntegerField()
    instrumentActual = models.IntegerField()
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