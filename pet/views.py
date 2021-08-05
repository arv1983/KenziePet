from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pet.models import Group, Animal, Characteristics
from .serializers import GroupSerializer, AnimalSerializers, CharacteristicSerializer
from django.db.utils import IntegrityError

from rest_framework import status, serializers


class GroupView(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
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
        
        groups_create = Group.objects.get_or_create(groups)[0]
        animal = Animal.objects.get_or_create(**serializer.validated_data,group=groups_create)[0]
        animal.characteristics.set(charac_list)
        

        # try:
        
        # except IntegrityError as e:
        #     print(e)
        #     return Response({ 'error': 'erro'}, status=status.HTTP_400_BAD_REQUEST)


  

        serializer = AnimalSerializers(animal)

        return Response(serializer.data)

    # FUNCIONANDOOOOOOOOOOOOO        
    # def post(self, request):
    #     print(request.data)
    #     serializer = GroupSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    #     group  = Group.objects.get_or_create(**serializer.validated_data)[0]
    #     serializer = GroupSerializer(group)
    #     return Response(serializer.data)

# class CharacteristicView(APIView):
#     def get(self, request):
#         charac = Characteristic.objects.all()
#         serializer = CharacteristicSerializer(charac)
#         return Response(serializer.data)


# Create your views here.



    # def post(self, request):
    #     serializer = ArtistSongsSerializer(data=request.data)
        
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     validated_data = serializer.validated_data
        
    #     songs = validated_data.pop('songs')
    #     try:
    #         artist = Artist.objects.get_or_create(**serializer.validated_data, user=request.user)[0]
    #     except IntegrityError:
    #         return Response({ 'error': 'User already link to an artist'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     song_list = []
    #     for song in songs:
    #         # Song.objects.get_or_create(**song, artist=artist)
    #         song = Song(**song, artist=artist)
    #         song_list.append(song)
            
    #     Song.objects.bulk_create(song_list)    
            
    #     serializer = ArtistSongsSerializer(artist)
    #     return Response(serializer.data)

