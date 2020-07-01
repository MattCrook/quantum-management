from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Attraction, Park, ParkAttractions, AttractionType
from django.contrib.auth.decorators import login_required


@login_required
def park_list_employees(request, park_id):
    if request.method == 'GET':
        all_park_attractions_in_park = ParkAttractions.objects.filter(park_id=park_id)
        attraction_types = AttractionType.objects.all()
        employees = Employee.objects.filter(park_id=park_id)
        park = Park.objects.get(pk=park_id)
        attractions = []

        for park_attraction in all_park_attractions_in_park:
            attraction_id = park_attraction.attraction_id
            all_attractions = Attraction.objects.filter(pk=attraction_id)
            attractions.append(all_attractions)
        all_roles = []
        for e in employees:
            role = e.role
            all_roles.append(role)
        roles = set(all_roles)



        template = 'parks/employees_in_park_list.html'
        context = {
            'park_attractions': all_park_attractions_in_park,
            'attractions': attractions,
            'attraction_types': attraction_types,
            'employees': employees,
            'park': park,
            'roles': roles
        }
        return render(request, template, context)
