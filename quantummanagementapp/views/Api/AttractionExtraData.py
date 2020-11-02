from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from quantummanagementapp.models import AttractionType, AttractionVisitors, AttractionWaitTimes


class AttractionWaitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionWaitTimes
        fields = ('id', 'current_wait_time', 'timestamp', 'attraction_id', 'park_id')
        depth = 1


class AttractionVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionVisitors
        fields = ('id', 'visit_timestamp', 'attraction_id')
        depth = 2


class AttractionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionType
        fields = ('id', 'name', 'manufacturer')
        depth = 1




class AttractionWaitTimesData(ModelViewSet):
    queryset = AttractionWaitTimes.objects.all()
    serializer_class = AttractionWaitTimeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['park_id']


class AttractionVisitorData(ModelViewSet):
    queryset = AttractionVisitors.objects.all()
    serializer_class = AttractionVisitorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['attraction_id', 'visit_timestamp']


class AttractionTypeData(ModelViewSet):
    queryset = AttractionType.objects.all()
    serializer_class = AttractionTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'manufacturer']
