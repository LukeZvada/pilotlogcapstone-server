"""View module for handling requests about new flight logs"""

from pilotlogapi.models import InBetween
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from pilotlogapi.models import PilotLogUsers, NewLog

class NewLogs(ViewSet):
    """Pilot Log New Flight Log"""

    def create(self, request):
        """Handle Post operations

        Returns:
            Response -- JSON serialized new flight log instance  
        """

        #Uses the toke passed in the `Authorization` header
        pilotLogUser = PilotLogUsers.objects.get(user=request.auth.user)
        # in_between = InBetween.objects.get(pk=request.data["inbetweenId"])

        log = NewLog()  
        log.PilotLogUserId = pilotLogUser
        log.date = request.data["date"]
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
        log.save()

        serializer = NewLogSerializer(
            log, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request):
        """Handle Get request to /newlog resource

        Returns:
            Response -- JSON serialized list of flight logs 
        """
        # Get all newlog records from the database
        log = NewLog.objects.all()
        serializer = NewLogSerializer(log, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single flight log -> /newlog/pk
        Returns:
            Response -- JSON serialized newlog  instance
        """
        try:
            # pk is a parameter to this function, and 
            # Django parses it from the URL route parameter
            # http://localhost:8000/newlog/2

            post = NewLog.objects.get(pk=pk)
            serializer = NewLogSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single flight log -> newlog/pk

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            post = NewLog.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except NewLog.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for a flight log -> newlog/pk

        Returns:
            Response -- Empty body with 204 status code
        """

        pilotLogUser = PilotLogUsers.objects.get(user=request.auth.user)

        # Doing mostly the same thing as the POST, but instead of 
        # creating a new instance of NewLog, I'm getting the newlog record
        # from the database whose primary key is `pk`
        log = NewLog.objects.get(pk=pk)
        log.PilotLogUserId = pilotLogUser
        log.date = request.data["date"]
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
        log.save()

        # 204 status code means everything worked by the
        # server is not sending back any data in the response

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = PilotLogUsers
        fields = ('id', )

# class PilotLogUserSerializer(serializers.ModelSerializer):
#     """JSON serializer for User Flight logs"""

#     user = UserSerializer(many=False)

#     class Meta:
#         model = User
#         fields = ('user', )

class InBetweenSerializer(serializers.ModelSerializer):
    """JSON serializer for inbetween stops during a flight"""
    class Meta:
        model = InBetween
        fields = ('airport')

class NewLogIdSerializer(serializers.ModelSerializer):
    """JSON serializer for inbetween stops during a flight"""
    class Meta:
        model = NewLog
        fields = ('id')

class NewLogSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
 
    Arguments:
        serializer type
    """
    PilotLogUserId = UserSerializer(many=False)
    
    class Meta:
        model = NewLog
        fields =('id', 'PilotLogUserId', 'date', 'make_and_model', 'aircraftId', 'fromAirport', 'to', 'landingsDay', 'landingsNight',
                'number_of_instrument_approaches', 'type_and_location', 'airplane_single_multi', 'airplane_single_multi_hours', 'instrumentActual',
                'simulator_hood', 'ftd_or_simulator', 'night', 'cross_country_all', 'cross_country_fivezero', 'pilot_in_command', 'solo',
                'ground_training', 'flight_training_received', 'flight_training_given', 'total_flight_time')
        depth = 1