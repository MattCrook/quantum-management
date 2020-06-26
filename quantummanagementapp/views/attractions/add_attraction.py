from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Park, Attraction, AttractionType, ParkAttractions
from django.contrib.auth.decorators import login_required


@login_required
def create_attraction(request, park_id):
    if request.method == 'GET':
        employees = Employee.objects.all()
        attractions = Attraction.objects.all()
        attraction_types = AttractionType.objects.all()
        park = Park.objects.get(pk=park_id)
        employee_attractions = EmployeeAttraction.objects.all()
        park_attractions = ParkAttractions.objects.filter(park_id=park_id)

        all_roles = []

        # loop thru all employees coming back and filter out the roles, delete duplicates
        for employee in employees:
            role = employee.role
            all_roles.append(role)
        roles = set(all_roles)

        template = 'attractions/add_attraction.html'
        context = {
            'employees': employees,
            'attractions': attractions,
            'attraction_types': attraction_types,
            'park': park,
            'employee_attractions': employee_attractions,
            'roles': roles,
            'park_attractions': park_attractions
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_attraction_type = AttractionType()
        new_attraction_type.name = form_data["name"]
        new_attraction_type.save()

        new_attraction = Attraction()
        new_attraction.name = form_data["name"]
        new_attraction.capacity = form_data["capacity"]
        new_attraction.current_operating_capacity = form_data["current_operating_capacity"]
        new_attraction.type = new_attraction_type.id
        new_attraction.save()


        new_park_attraction = ParkAttractions()
        new_park_attraction.park = park_id
        new_park_attraction.attraction = new_attraction.id
        new_park_attraction.save()


        return redirect(reverse('quantummanagementapp:park', kwargs={'park_id': park_id}))
