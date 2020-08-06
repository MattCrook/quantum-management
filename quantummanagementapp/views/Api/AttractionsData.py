from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from quantummanagementapp.models import Attraction


class AttractionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        # url = serializers.HyperlinkedIdentityField(
        #     view_name='park-detail',
        #     lookup_field='id',
        # )
        fields = ('id', 'name', 'capacity', 'current_operating_capacity', 'type', 'park', )
        depth = 2


class AttractionData(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'type_id', 'park_id', 'name']
