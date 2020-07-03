import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from quantummanagementapp.models import Employee, EmployeeAttraction, Attraction, Park
from django.http import HttpResponseServerError, HttpResponse
from rest_framework import status


@login_required
def get_employee_details(request, employee_id):
    if request.method == 'GET':
        employee = Employee.objects.get(pk=employee_id)
        attractions = Attraction.objects.all()
        employee_attractions = EmployeeAttraction.objects.filter(employee_id=employee_id)
        current_date = datetime.date.today()

        template = 'employees/employee_details.html'
        context = {
            "employee": employee,
            "current_date": current_date,
            "attractions": attractions,
            "employee_attractions": employee_attractions
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
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
            try:
                employee = Employee.objects.get(pk=employee_id)
                employee.delete()
                return redirect(reverse('quantummanagementapp:employee_list'))
            except Employee.DoesNotExist as ex:
                return HttpResponseServerError({'Error: not found': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return HttpResponseServerError({'Oops!: Something went wrong.': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
