##first API
from rest_framework.views import APIView
from rest_framework.response import Response
#post method import below
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name} bitch'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Sepcific url pk lote lo pk=None pyit, pk = id of object to update
        Handle updating an object. will update entire object with what u put in req"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Updating the part of the object provided"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """deleting an object"""
        return Response({'method':'delete'})
