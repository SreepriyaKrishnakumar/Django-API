from django.shortcuts import render
from rest_framework.views import APIView
from contactlist.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserRegisterView(APIView):

    def post(self,request):

        serializer = RegisterSerializer(data = request.data)

        print(request.data)

        if serializer.is_valid():

            print("validated")

            user = serializer.save()         

            token = Token.objects.get(user_id = user.id)

            return Response({"token":token.key},status=status.HTTP_200_OK)
        
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class ConatctListCreate(APIView):

    def get(self,request):

        contact = ContactModel.objects.all()

        serializer = ContactSerializer(contact,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def post(self,request):

        serializer = ContactSerializer(data = request.data)

        if serializer.is_valid():

            res = serializer.save()

            return Response({"message":"One Data Added to Contact"},status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_404_NOT_FOUND)


class ContactDeletUpdateView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        data = ContactModel.objects.get(id=id)

        serializer = ContactSerializer(data)

        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,**kwargs):

        id = kwargs.get("pk")

        data = ContactModel.objects.get(id=id)

        serializer = ContactSerializer(data,request.data)

        if serializer.is_valid():

            res = serializer.save()

            return Response({"message":"Updated"},status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)



    def delete(self,request,**kwargs):

        id = kwargs.get("pk")

        data = ContactModel.objects.get(id=id).delete()

        return Response({"message":"Deleted"},status=status.HTTP_202_ACCEPTED)
    

class FavoriteContactView(APIView):

    def get(self,request):

        data = ContactModel.objects.filter(status=True)

        serializer = ContactSerializer(data,many=True)

        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)