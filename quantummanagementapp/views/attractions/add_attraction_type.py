from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Park, Attraction, AttractionType, ParkAttractions
from django.contrib.auth.decorators import login_required


@login_required
def attraction_type_list(request, park_id):
    if request.method == 'GET':
        attraction_types = AttractionType.objects.all()
        template = 'attractions/add_attraction.html'
        context = {
            'attraction_types': attraction_types
        }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        new_attraction_type = AttractionType()
        new_attraction_type.name = form_data['type']
        new_attraction_type.save()
        return redirect(reverse('quantummanagementapp:create_attraction', kwargs={'park_id': park_id}))
