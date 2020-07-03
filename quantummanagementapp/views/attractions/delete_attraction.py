from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Park, Attraction, AttractionType, ParkAttractions
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError, HttpResponse
from rest_framework import status



@login_required
def delete_attraction(request, park_id):
    if request.method == 'GET':
        park = Park.objects.get(pk=park_id)
        template = 'attractions/add_attraction.html'
        context = {
            'park': park,
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        park = Park.objects.get(pk=park_id)
        park.attraction = form_data["attractions"]

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
            attraction_to_delete = form_data["attractions"]
            attraction = Attraction.objects.get(pk=attraction_to_delete)
            attraction.delete()
            return redirect(reverse('quantummanagementapp:create_attraction', kwargs={'park_id': park_id}))
