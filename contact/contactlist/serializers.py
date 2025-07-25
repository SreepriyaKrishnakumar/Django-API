from rest_framework import serializers
from contactlist.models import *
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","password"]


    def create(self,validated_data):
        
        user_obj = User.objects.create_user(**validated_data)

        return user_obj
    

class ContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = ContactModel

        fields = "__all__"

        read_only_fields = ["id"]