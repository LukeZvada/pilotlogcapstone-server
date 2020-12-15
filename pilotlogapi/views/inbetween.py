"""View module for handling requests about inbetween stops on flight log"""
from django.http.response import HttpResponseServerError
from pilotlogapi.models import inbetween
from pilotlogapi.models.newlog import NewLog
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

class InBetweenView(ViewSet):
    
    def create(self, request):
        """Handle POST request for in_between stops during a flight -> /inbetween"""


        NewLogId = NewLog.objects.get(pk=request.data["NewLogId"])
        
        in_between = inbetween.InBetween()
        in_between.NewLogId = NewLogId
        in_between.airport = request.data["airport"]

        try:
            in_between.save()
            serializer = InBetweenSerializer(in_between, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle get requests for all inbetween stops during flights -> /inbetween"""

        in_between = inbetween.InBetween.objects.all()
        

        serializer = InBetweenSerializer(in_between, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle Get requests for single stop during a flight -> /inbetween/pk

        Returns:
            Response -- JSON serialized category instance
        """
        try:
            in_between = inbetween.InBetween.objects.get(pk=pk)
            serializer = InBetweenSerializer(in_between, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
            
    def destroy(self, request, pk=None):
        """Handles delete request for single inbetween stop during a flight -> /inbetween/pk """
        try:
            in_between = inbetween.InBetween.objects.get(pk=pk)
            in_between.delete()

            return Response({},status=status.HTTP_204_NO_CONTENT)

        except inbetween.InBetween.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handles PUT request for single inbetween stop during a flight -> /inbetween/pk """

        in_between = inbetween.InBetween.objects.get(pk=pk)
        in_between.airport = request.data['airport']

        in_between.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)



class InBetweenSerializer(serializers.ModelSerializer):
    """JSON serializer for inbetween stops during a flight
 
    Arguments:
        serializer type
    """
    
    class Meta:
        model = inbetween.InBetween
        fields =('id', 'NewLogId', 'airport')
        depth = 1
