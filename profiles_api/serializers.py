from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our api view"""
    name = serializers.CharField(max_length=10)

#Model Serializer which is ez to work with django db


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile Object"""
    #You need Meta to point to models if connecting with model
    class Meta:
        model = models.UserProfile
        fields = ('name', 'id', 'email', 'password')
        #password retrieve only when making a new user so,
        extra_kwargs = {
            'password': {
                'write_only': True,
                #cannot read or retrieve (get is disabled)
                'style': {'input_type': 'password'}
            }
        }
        #Model serializer doesnt censor password as hash

        #default create function ko override lote pee create user func lote mel to hash the password
    #this overrides the create function taking in the create_user function from the models
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

