from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pet.models import Group, Animal, Characteristics
from .serializers import GroupSerializer, AnimalSerializers, CharacteristicSerializer
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import status, serializers


class GroupView(APIView):
    def get(self, request, animal_id=''):
        if animal_id:
            animal = Animal.objects.filter(id=animal_id)
            if not animal:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            animal = Animal.objects.all()
        
        
        serializer = AnimalSerializers(animal, many=True)
        
        return Response(serializer.data)


    def post(self, request):
        
        
        serializer = AnimalSerializers(data=request.data)
        

        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        groups = validated_data.pop('group')
        characs = validated_data.pop('characteristics')

        charac_list = []
        for charac in characs:
            charac_c = Characteristics.objects.get_or_create(**charac)[0]
            charac_list.append(charac_c)
        
        groups_create = Group.objects.get_or_create(**groups)[0]
        animal = Animal.objects.get_or_create(**serializer.validated_data,group=groups_create)[0]
        animal.characteristics.set(charac_list)


        serializer = AnimalSerializers(animal)

        return Response(serializer.data, status=201)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)
        
        animal.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
