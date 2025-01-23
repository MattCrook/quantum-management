from django.shortcuts import render
from quantummanagementapp.models import Employee, EmployeeAttraction, Attraction, Park, ParkAttractions, AttractionType
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseServerError, HttpResponse
from rest_framework import status


@login_required
def park_category_details_list(request, park_id, type_id):
    if request.method == 'GET':
        park = Park.objects.get(pk=park_id)
        park_attractions = ParkAttractions.objects.filter(park_id=park_id)
        attractions = Attraction.objects.filter(type_id=type_id)
        employees = Employee.objects.filter(park_id=park_id)
        employee_attractions = EmployeeAttraction.objects.all()
        type = AttractionType.objects.get(pk=type_id)


        template = 'parks/park_attraction_details.html'
        context = {
            'park': park,
            'attractions': attractions,
            'park_attractions': park_attractions,
            'employees': employees,
            'employee_attractions': employee_attractions,
            'type': type
        }
        return render(request, template, context)
