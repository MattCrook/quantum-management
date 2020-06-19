from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee
from django.contrib.auth.decorators import login_required
from .helpers import add_employee


@login_required
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        roles = list()

        for employee in employees:
            role = employee.role
            if role not in roles:
                roles.append(role)
            else:
                pass

        template = 'employees/employee_list.html'
        context = {
            'employees': employees,
            'roles': roles
        }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        print('FORMDATA', form_data)

        # Getting the ID of the admin user, not the auth user thru the auth user
        user_id = request.user.admin_user.id
        print('ADMINUSERID', user_id)

        # creating empty class object w/ ORM, assinging it the fields coming back from the form data. Same as doing in inline in parens.
        new_employee = Employee.objects.create()
        new_employee.first_name = form_data["first_name"]
        new_employee.last_name= form_data["last_name"]
        new_employee.role = form_data["max_height"]
        new_employee.compensation = form_data["compensation"]
        new_employee.start_date = form_data["date"]
        new_employee.is_salary = form_data["is_salary"]
        new_employee.is_hourly = form_data["is_hourly"]
        new_employee.admin_user_id = user_id

        new_employee.save()
        return redirect(reverse('quantummangementapp:employee_list'))
