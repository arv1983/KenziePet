from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pet.models import Group, Characteristic
from .serializers import GroupSerializer
from .serializers import CharacteristicSerializer

class GroupView(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

class CharacteristicView(APIView):
    def get(self, request):
        name = Characteristic.objects.all()
        serializer = CharacteristicSerializer(name)
        return Response(serializer.data)


# Create your views here.
