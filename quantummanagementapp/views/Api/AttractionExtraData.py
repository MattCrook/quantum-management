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
        fields = ('id', 'current_wait_time', 'timestamp', 'attraction_id', 'park_id', 'attraction')
        depth = 2


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


class AttractionWaitTimesData(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            attraction_wait_time = AttractionWaitTimes.objects.get(pk=pk)
            serializer = AttractionWaitTimeSerializer(
                attraction_wait_time, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        attraction_wait_times = AttractionWaitTimes.objects.all()

        park_id = self.request.query_params.get('park_id', None)
        if park_id is not None:
            attraction_wait_times = attraction_wait_times.filter(park_id=park_id)

        attraction_id = self.request.query_params.get('attraction_id', None)
        if attraction_id is not None:
            attraction_wait_times = attraction_wait_times.filter(attraction_id=attraction_id)

        serializer = AttractionWaitTimeSerializer(attraction_wait_times, many=True, context={'request': request})
        return Response(serializer.data)


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
