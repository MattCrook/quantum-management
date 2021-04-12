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
        fields = ('id', 'name', 'capacity',
                  'current_operating_capacity', 'type', 'park')
        depth = 2


class AttractionData(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            attraction = Attraction.objects.get(pk=pk)
            name = self.request.query_params.get('name', None)
            if name is not None:
                attraction = attraction.filter(name=name)

            park_id = self.request.query_params.get('park_id', None)
            if park_id is not None:
                attraction = attraction.filter(park_id=park_id)

            type_id = self.request.query_params.get('type_id', None)
            if type_id is not None:
                attraction = attraction.filter(type_id=type_id)

            serializer = AttractionDataSerializer(
                attraction, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        attractions = Attraction.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            attractions = attractions.filter(name=name)

        park_id = self.request.query_params.get('park_id', None)
        if park_id is not None:
            attractions = attractions.filter(park_id=park_id)

        type_id = self.request.query_params.get('type_id', None)
        if type_id is not None:
            attractions = attractions.filter(type_id=type_id)

        serializer = AttractionDataSerializer(
            attractions, many=True, context={'request': request})
        return Response(serializer.data)
