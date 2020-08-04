from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from quantummanagementapp.models import Visitor, VisitorCheckOut

class VisitorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('id', 'check_in', 'ticket_price', 'park_id')
        depth = 1

class VisitorCheckoutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorCheckOut
        fields = ('id', 'checkout_timestamp', 'park_id')
        depth = 1



class VisitortData(ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email']


class VisitorCheckoutData(ModelViewSet):
    queryset = VisitorCheckOut.objects.all()
    serializer_class = VisitorCheckoutDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email']
