##first API
from rest_framework.views import APIView
from rest_framework.response import Response
#post method import below
from rest_framework import status, viewsets
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication

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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Returns a hello message"""
        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello function"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name} serializer view bitch'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method':'GET'})
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http-method': 'DELETE'})

#We make it same as above, connect to serializer stuff, here the modelviewset gets queryset, which obj to manage.
class UserProfileViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #authentications added below
    authentication_classes = (TokenAuthentication,)
    #authentication=how user is authenticated/ permission=how user has what permissions
    permission_classes = (permissions.UpdateOwnProfile,)
    #passes through permissions.py file
