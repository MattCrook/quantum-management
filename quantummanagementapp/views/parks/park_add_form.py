from quantummanagementapp.models import Employee, EmployeeAttraction, Park, Attraction
from django.shortcuts import render, redirect, reverse
import datetime
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseServerError
from rest_framework import status


@login_required
def park_form(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        parks = Park.objects.all()
        attractions = Attraction.objects.all()
        template = "parks/park_add_form.html"
        context = {
            'employees': employees,
            'attractions': attractions,
            'parks': parks,
        }
        return render(request, template, context)

@login_required
def park_edit_form(request, park_id):
    if request.method == 'GET':
        park = Park.objects.get(pk=park_id)
        employees = Employee.objects.all()
        attractions = Attraction.objects.all()
        template = "parks/park_add_form.html"
        context = {
            'employees': employees,
            'attractions': attractions,
            'park': park,
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        if ("actual_method" in form_data and form_data["actual_method"] == "PUT"):
            park = Park.objects.get(pk=park_id)
            employees = Employee.objects.all()
            attractions = Attraction.objects.all()

            adminuser_id = request.user.user.id

            park.name = form_data['name']
            park.state = form_data['state']
            park.max_capacity = form_data['max_capacity']
            park.number_of_attractions = form_data['number_of_attractions']

            park.save()
            return redirect(reverse('quantummanagementapp:parks'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
            park = Employee.objects.get(pk=park_id)
            park.delete()
            return redirect(reverse('quantummanagementapp:parks'))
