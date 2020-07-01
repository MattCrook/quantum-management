from quantummanagementapp.models import Employee, EmployeeAttraction, Park, Attraction, Roles, ParkAttractions
from django.shortcuts import render, redirect, reverse
import datetime
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseServerError
from rest_framework import status





@login_required
def employee_form(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        parks = Park.objects.all()
        attractions = Attraction.objects.all()
        all_roles = Roles.objects.all()
        park_attractions = ParkAttractions.objects.all()

        template = "employees/employee_form.html"
        context = {
            'employees': employees,
            'attractions': attractions,
            'parks': parks,
            'all_roles': all_roles,
            'park_attractions': park_attractions,
        }
        return render(request, template, context)


@login_required
def employee_edit_form(request, employee_id):
    if request.method == 'GET':
        employee = Employee.objects.get(pk=employee_id)
        employee_attractions = EmployeeAttraction.objects.filter(employee_id=employee_id)
        attractions = Attraction.objects.all()
        parks = Park.objects.all()
        employees = Employee.objects.all()
        roles = Roles.objects.all()

        all_roles = []
        # filter out duplicates
        # could also convert to set to get rid of duplicates
        # all_roles = set(roles)
        for e in employees:
            if e.role not in all_roles:
                all_roles.append(e.role)

        template = "employees/employee_form.html"
        context = {
            'employee': employee,
            'employee_attractions': employee_attractions,
            'attractions': attractions,
            'parks': parks,
            'all_roles': all_roles
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        if ("actual_method" in form_data and form_data["actual_method"] == "PUT"):
            employee = Employee.objects.get(pk=employee_id)
            park_id = employee.park_id
            park = Park.objects.get(pk=park_id)
            employee_attraction = EmployeeAttraction.objects.get(employee_id=employee_id)
            admin_user_id = request.user.user.id

            employee.first_name = form_data["first_name"]
            employee.last_name = form_data["last_name"]
            employee.role = form_data["role"]
            employee.start_date = form_data["start_date"]
            employee.admin_user_id = admin_user_id
            employee.compensation = form_data["compensation"]
            employee.pay_rate = form_data["pay_rate"]

            employee.park_id = form_data["parks"]
            employee_attraction.attraction_id = form_data["employee_attraction"]

            employee.save()
            employee_attraction.save()
            return redirect(reverse('quantummanagementapp:employee_list'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
            employee = Employee.objects.get(pk=employee_id)
            employee.delete()
            return redirect(reverse('quantummanagementapp:employee_list'))
