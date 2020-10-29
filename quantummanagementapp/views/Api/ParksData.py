from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from quantummanagementapp.models import Park, ParkAttractions

class ParkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ('id', 'name', 'state', 'max_capacity', 'number_of_attractions')
        depth = 1


class ParkData(ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']



class ParkAttractionsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkAttractions
        fields = ('id', 'attraction', 'park')
        depth = 2


class ParkAttractionsData(ModelViewSet):
    queryset = ParkAttractions.objects.all()
    serializer_class = ParkAttractionsDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['park_id']
