"""In between model module to handle stops during a flight for fuel, landings, etc."""
from django.db import models


class InBetween(models.Model):
    """InBetween database model that handles inbetween stops during a flight"""
    NewLogId = models.ForeignKey("NewLog", on_delete=models.CASCADE)
    airport = models.CharField(max_length=50)