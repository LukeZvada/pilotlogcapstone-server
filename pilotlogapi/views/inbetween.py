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
        """Handle POST request for in_between stops during a flight"""


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
        """Handle get requests for categories """

        in_between = inbetween.InBetween.objects.all()
        

        serializer = InBetweenSerializer(in_between, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle Get requests for single category

        Returns:
            Response -- JSON serialized category instance
        """
        try:
            # pk is a parameter to this function, and
            # Django parses it from the URL route parameter
            # http://localhost:8000/categories/2
            #
            # The `2` at the end of the route becomes `pk`

            in_between = inbetween.InBetween.objects.get(pk=pk)
            serializer = InBetweenSerializer(in_between, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
            
    # def destroy(self, request, pk=None):
    #     try:
    #         category = Category.objects.get(pk=pk)
    #         category.delete()

    #         return Response({},status=status.HTTP_204_NO_CONTENT)

    #     except Category.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    #     except Exception as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def update(self, request, pk=None):
        
    #     category = Category.objects.get(pk=pk)
    #     category.label = request.data['label']

    #     category.save()

    #     return Response({}, status=status.HTTP_204_NO_CONTENT)



# class InBetweenSerializer(serializers.HyperlinkedModelSerializer):
#     """JSON serializer for categories"""

#     class Meta:
#         model = InBetweenView
#         url = serializers.HyperlinkedIdentityField(
#             view_name='inbetween',
#             lookup_field='id'
#         )
#         fields = ('id', 'NewLogId', 'airport')


class InBetweenSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
 
    Arguments:
        serializer type
    """
    
    class Meta:
        model = inbetween.InBetween
        fields =('id', 'NewLogId', 'airport')
        depth = 1
