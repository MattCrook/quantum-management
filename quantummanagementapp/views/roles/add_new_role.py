from quantummanagementapp.models import Employee, EmployeeAttraction, Park, Attraction, Roles
from django.shortcuts import render, redirect, reverse
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def role_list(request):
    if request.method == 'GET':
        roles = Roles.objects.all()

        template = 'roles/add_new_role.html'
        context = {
            'roles': roles,
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        user = request.user
        new_role = Roles()
        new_role.name = form_data["name"]
        new_role.save()
        return redirect(reverse('quantummanagementapp:employee_form'))
