from django.core.exceptions import ValidationError
from django.http import request
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from pilotlogapi.models import PilotLogUsers
from django.contrib.auth.models import User
import uuid
import base64
from django.core.files.base import ContentFile



class PilotLogProfile(ViewSet):
    

    def retrieve(self, request, pk=None):
        """Handle GET requests for single profile

        Returns:
            Response -- JSON serialized profile instance
        """
        
        try:
            user = PilotLogUsers.objects.get(pk=pk)
            serializer = PilotLogProfileSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def update(self, request, pk=None):
        """Handle Put operations

        Returns:
            Response -- JSON serialized post instance
        """

        pilotloguser = PilotLogUsers.objects.get(user=request.auth.user)

        # format, imgstr = request.data['profile_image_url'].split(';base64,')
        # ext = format.split('/')[-1]
        # data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["profile_id"]}-{uuid.uuid4()}.{ext}')
        # pilotloguser.profile_image_url = data

        try:
            pilotloguser.save()
            serializer = PilotLogProfileSerializer (pilotloguser, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class PilotLogProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_staff')

class PilotLogProfileSerializer(serializers.ModelSerializer):

    user = PilotLogProfileUserSerializer(many=False)

    class Meta:
        model = PilotLogUsers
        fields = ('id', 'bio', 'profile_image_url', 'created_on',
                'active', 'user')
        depth = 1