from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Attraction, Park, ParkAttractions, AttractionType
from django.contrib.auth.decorators import login_required


@login_required
def park_list(request):
    if request.method == 'GET':
        attractions = Attraction.objects.all()
        attraction_types = AttractionType.objects.all()
        employees = Employee.objects.all()
        parks = Park.objects.all()

        template = 'parks/park_list.html'
        context = {
            'attractions': attractions,
            'attraction_types': attraction_types,
            'employees': employees,
            'parks': parks
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        adminuser_id = request.user.user.id

        new_park = Park()
        new_park.name = form_data['name']
        new_park.state = form_data['state']
        new_park.max_capacity = form_data['max_capacity']
        new_park.number_of_attractions = form_data['number_of_attractions']

        new_park.save()
        return redirect(reverse('quantummanagementapp:parks'))
