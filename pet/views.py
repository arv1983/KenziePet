from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pet.models import Group, Characteristic
from .serializers import GroupSerializer
from .serializers import CharacteristicSerializer
from rest_framework import status

class GroupView(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        print(request.data)
        serializer = GroupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        group = Group.objects.get_or_create(**serializer.validated_data)[0]
        serializer = GroupSerializer(group)

        return Response(serializer.data)


class CharacteristicView(APIView):
    def get(self, request):
        charac = Characteristic.objects.all()
        serializer = CharacteristicSerializer(charac)
        return Response(serializer.data)


# Create your views here.
