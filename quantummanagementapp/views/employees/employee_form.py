from quantummanagementapp.models import Employee, EmployeeAttraction, Park, Attraction
from django.shortcuts import render, redirect, reverse
import datetime
from django.contrib.auth.decorators import login_required
from django import forms

@login_required
def employee_form(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        parks = Park.objects.all()
        attractions = Attraction.objects.all()
        # add employee_attraction join to have option of creating a new row to add employee to attraction when adding

        template = "employees/employee_form.html"
        context = {
            'employees': employees,
            'attractions': attractions,
            'parks': parks
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
        # start_date_employee = datetime.datetime.strptime(employee.start_date, '%Y-%m-%d').date()

        all_roles = []

        for employee in employees:
            if employee.role not in all_roles:
                all_roles.append(employee.role)

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
        if (
            "actual_method" in form_data
             and form_data["actual_method"] == "PUT"
        ):
            employee = Employee.objects.get(pk=employee_id)
            admin_user_id = request.user.user.id
            employee_attraction = EmployeeAttraction.objects.filter(employee_id=employee_id)

            employee.first_name = form_data["first_name"]
            employee.last_name= form_data["last_name"]
            employee.role = form_data["role"]
            employee.compensation = form_data["compensation"]
            employee.start_date = form_data["start_date"]
            employee.pay_rate = form_data["pay_rate"]
            # employee.park_id = form_data["park_id"]
            employee.admin_user_id = admin_user_id

            employee.save()
            return redirect(reverse('quantummanagementapp:employee_list'))

        if ("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
            employee_to_be_deleted = Employee.objects.get(pk=employee_id)
            employee_to_be_deleted.delete()
            return redirect(reverse('quantummanagementapp:employee_list'))
