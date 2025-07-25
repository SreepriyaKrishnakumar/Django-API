from django.shortcuts import render
from rest_framework.views import APIView
from eventapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserRegistation(APIView):

    def post(self,request):

        serializer_obj =  UserSerializer(data = request.data)

        if serializer_obj.is_valid():

            user = serializer_obj.save()

            return Response({"message":"User created"},status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class EventCreateListView(APIView):

    def get(self,request):

        event = EventModel.objects.all()

        serializer = EventSerializer(event,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
        

    def post(self,request):

        serializer = EventSerializer(data = request.data)

        if serializer.is_valid():

            event = serializer.save()

            return Response({"message":"event created"},status=status.HTTP_200_OK)



class EventUpdateDeleteView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        event = EventModel.objects.get(id = id)

        serializer = EventSerializer(event)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def put(self,request,**kwargs):

        id = kwargs.get("pk")

        event = EventModel.objects.get(id=id)

        serializer = EventSerializer(event,request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"message":"Updated"},status=status.HTTP_200_OK)
        

    def delete(self,request,**kwargs):

        id = kwargs.get("pk")

        event = EventModel.objects.get(id=id).delete()

        return Response({"message":"Deleted"},status=status.HTTP_200_OK)
    
