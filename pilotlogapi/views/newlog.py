"""View module for handling requests about new flight logs"""

from django.core.exceptions import ValidationError
from django.http import request
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from pilotlogapi.models import PilotLogUsers

class NewLogs(ViewSet):
    """Pilot Log New Flight Log"""

    def create(self, request):
        """Handle Post operations

        Returns:fds
            Response -- JSON serialized post instancefdsfds  
        """

        #Uses the toke passed in the `Authorization` header
        pilotLogUser = PilotLogUsers.objects.get(user=request.auth.user)

        # Creat a new Python instance of the Post class
        # and set its properties from what was sent in the
        # body of the request from the client.

        log = NewLogs()  
        log.date= request.data['date']
        log.make_and_model = request.data['make_and_model']
        log.aircraftId = request.data['aircraftId']
        log.fromAirport = request.data['fromAirport']
        log.to = request.data['to'] 
        log.landingsDay = request.data['landingsDay'] 
        log.landingsNight = request.data['landingsNight'] 
        log.number_of_instrument_approaches = request.data['number_of_instrument_approaches'] 
        log.type_and_location = request.data['type_and_location'] 
        log.airplane_single_multi = request.data['airplane_single_multi'] 
        log.airplane_single_multi_hours = request.data['airplane_single_multi_hours'] 
        log.instrumentActual = request.data['instrumentActual'] 
        log.simulator_hood = request.data['simulator_hood'] 
        log.ftd_or_simulator = request.data['ftd_or_simulator'] 
        log.night = request.data['night'] 
        log.cross_country_all = request.data['cross_country_all'] 
        log.cross_country_fivezero = request.data['cross_country_fivezero'] 
        log.pilot_in_command = request.data['pilot_in_command'] 
        log.solo = request.data['solo'] 
        log.ground_training = request.data['ground_training'] 
        log.flight_training_received = request.data['flight_training_received'] 
        log.flight_training_given = request.data['flight_training_given'] 
        log.total_flight_time = request.data['total_flight_time'] 
        log.pilotLogUser = pilotLogUser


        # Try to save the new post to the database, then
        # serialize the post instance as JSON, and send the
        # JSON as a response to the client request
        try:
            log.save()
            serializer = NewLogSerializer (log, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class PilotLogUserSerializer(serializers.ModelSerializer):
    """JSON serializer for User Posts"""

    user = UserSerializer(many=False)

    class Meta:
        model = PilotLogUsers
        fields = ('user', )


class NewLogSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializer type
    """
    pilotLogUserId = PilotLogUserSerializer(many=False)
    
    class Meta:
        model = NewLogs
        fields =('id', 'PilotLogUserId', 'date', 'make_and_model', 'aircraftId', 'fromAirport', 'to', 'landingsDay', 'landingsNight'
                'number_of_instrument_approaches', 'type_and_location', 'airplane_single_multi', 'airplane_single_multi_hours', 'instrumentActual',
                'simulator_hood', 'ftd_or_simulator', 'night', 'cross_country_all', 'cross_country_fivezero', 'pilot_in_command', 'solo',
                'ground_training', 'ground_training_received', 'flight_time_given', 'total_flight_time')
        depth = 1