from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Employee, EmployeeAttraction, Park
from django.contrib.auth.decorators import login_required


@login_required
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        all_roles = []
        for employee in employees:
            role = employee.role
            all_roles.append(role)
        roles = set(all_roles)

        template = 'employees/employee_list.html'
        context = {
            'employees': employees,
            'roles': roles
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Getting the ID of the admin user, (not authuser) thru the auth user
        adminuser_id = request.user.user.id

        # creating empty class object w/ ORM, assinging it the fields coming back from the form data. Same as doing in inline in parens class...
        new_employee = Employee()
        new_employee.first_name = form_data["first_name"]
        new_employee.last_name = form_data["last_name"]
        new_employee.role = form_data["role"]
        new_employee.compensation = form_data["compensation"]
        new_employee.start_date = form_data["start_date"]
        new_employee.pay_rate = form_data["pay_rate"]
        new_employee.admin_user_id = adminuser_id

        park = Park()
        new_employee.park_id = form_data["parks"]

        new_employee.save()
        employee_attraction = EmployeeAttraction()
        employee_attraction.attraction_id = form_data["employee_attraction"]
        employee_attraction.employee_id = new_employee.id

        employee_attraction.save()
        return redirect(reverse('quantummanagementapp:employee_list'))
