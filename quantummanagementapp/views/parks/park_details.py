from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Attraction, Park, ParkAttractions, AttractionType
from django.contrib.auth.decorators import login_required

@login_required
def park_details(request, park_id):
    park = Park.objects.get(pk=park_id)
    park_attractions = ParkAttractions.objects.filter(park_id=park_id)
    attraction_types = AttractionType.objects.all()
    employees = Employee.objects.filter(park_id=park_id)
    employee_attractions = EmployeeAttraction.objects.all()


# get attraction types
# need attractions in the specific park
# take those filtered list and compare to type table
    # for park_attraction in park_attractions:
    #     attraction_id = park_attraction.
    #     attractions = Attraction.objects.filter(pk=attraction)

    template = 'parks/park_details.html'
    context = {
        'park': park,
        'park_attractions': park_attractions,
        'attraction_types': attraction_types,
        'employees': employees,
        'employee_attractions': employee_attractions,
    }
    return render(request, template, context)
