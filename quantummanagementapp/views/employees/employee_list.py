from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction
from django.contrib.auth.decorators import login_required


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

        # Getting the ID of the admin user, not the auth user thru the auth user
        adminuser_id = request.user.user.id

        # creating empty class object w/ ORM, assinging it the fields coming back from the form data. Same as doing in inline in parens.
        new_employee = Employee()
        new_employee.first_name = form_data["first_name"]
        new_employee.last_name= form_data["last_name"]
        new_employee.role = form_data["role"]
        new_employee.compensation = form_data["compensation"]
        new_employee.start_date = form_data["start_date"]
        new_employee.pay_rate = form_data["pay_rate"]
        # new_employee.park_id = form_data["park_id"]
        new_employee.admin_user_id = adminuser_id

        # employee_attraction = EmployeeAttraction()
        # employee_attraction.attraction_id = form_data["attraction_id"]
        # employee_attraction.employee_id = new_employee.id

        new_employee.save()
        return redirect(reverse('quantummanagementapp:employee_list'))
