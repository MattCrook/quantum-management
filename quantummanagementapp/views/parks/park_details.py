from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Attraction, Park, ParkAttractions, AttractionType
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError, HttpResponse
from rest_framework import status


@login_required
def park_details(request, park_id):
    if request.method == 'GET':
        park = Park.objects.get(pk=park_id)
        park_attractions = ParkAttractions.objects.filter(park_id=park_id)
        attraction_types = AttractionType.objects.all()
        employees = Employee.objects.filter(park_id=park_id)
        employee_attractions = EmployeeAttraction.objects.all()

        template = 'parks/park_details.html'
        context = {
            'park': park,
            'park_attractions': park_attractions,
            'attraction_types': attraction_types,
            'employees': employees,
            'employee_attractions': employee_attractions,
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        if ("actual_method" in form_data and form_data["actual_method"] == "PUT"):
            park = Park.objects.get(pk=park_id)
            park_attractions = ParkAttractions.objects.filter(park_id=park_id)
            attraction_types = AttractionType.objects.all()
            employees = Employee.objects.filter(park_id=park_id)
            employee_attractions = EmployeeAttraction.objects.all()

            park.name = form_data["name"]
            park.state = form_data["state"]
            park.max_capacity = form_data["max_capacity"]
            park.number_of_attractions = form_data["number_of_attractions"]

            park.save()
            return redirect(reverse('quantummanagementapp:parks'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
            try:
                park = Park.objects.get(pk=park_id)
                park.delete()
                return redirect(reverse('quantummanagementapp:parks'))
            except Employee.DoesNotExist as ex:
                return HttpResponseServerError({'Error: not found': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return HttpResponseServerError({'Oops!: Something went wrong.': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return redirect(reverse('quantummanagementapp:parks'))
