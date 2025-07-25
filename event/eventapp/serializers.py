from rest_framework import serializers
from eventapp.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","password"]


    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)

        return user
    

class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = EventModel

        fields = "__all__"

        read_only_fields = ["id"]