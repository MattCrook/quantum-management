import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from quantummanagementapp.models import Employee, EmployeeAttraction, Attraction



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

    # elif request.method == 'POST':
    #     form_data = request.POST
    #     if (
    #         "actual_method" in form_data
    #          and form_data["actual_method"] == "PUT"
    #     ):
    #         employee = Employee.objects.get(pk=employee_id)
    #         user_id = request.user.adminuser.id
    #         employee_attraction = EmployeeAttraction.objects.filter(employee_id=employee_id)

    #         employee.first_name = form_data["first_name"]
    #         employee.last_name= form_data["last_name"]
    #         employee.role = form_data["max_height"]
    #         employee.compensation = form_data["compensation"]
    #         employee.start_date = form_data["date"]
    #         employee.is_salary = form_data["is_salary"]
    #         employee.is_hourly = form_data["is_hourly"]
    #         employee.park_id = form_data["park_id"]
    #         employee.admin_user_id = user_id

    #         employee.update()
    #         employee.save()
    #         return redirect(reverse('quantummanagementapp:employee_list'))

    #     if ("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
    #         employee_to_be_deleted = Employee.objects.get(pk=employee_id)
    #         employee_to_be_deleted.delete()
    #         return redirect(reverse('quantummanagementapp:employee_list'))






    
