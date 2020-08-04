from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from quantummanagementapp.models import Employee, EmployeeAttraction

class EmployeeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'url', 'first_name', 'last_name', 'role', 'start_date', 'pay_rate', 'compensation', 'park_id', 'admin_user_id')
        depth = 1


class EmployeeData(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email']



class EmployeeAttractionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAttraction
        fields = ('id', 'attraction_id', 'employee_id')
        depth = 1


class EmployeeAttractionData(ViewSet):
    queryset = EmployeeAttraction.objects.all()
    serializer_class = EmployeeAttractionDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email']
