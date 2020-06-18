import json
from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseServerError
from quantummanagementapp.models import AdminUser, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        print("EMPLOYEES", employees)

        role_groups = {}
        roles = list()

        for employee in employees:
            role = employee.role
            if role not in roles:
                roles.append(role)
            else:
                pass
        print("roles", roles)






        # for employee in employees:
        #     if employee.id not in role_groups:
        #         role_groups[employee.id] = role
        #         role_groups[employee.id].role.append(employee)
        #     else:
        #         role_groups[employee.id].role.append(employee)
        # print("ROLEGOUPS", role_groups)




        # Iterate the list of tuples
        # for (library, book) in libraries:

    # If the dictionary does have a key of the current
    # library's `id` value, add the key and set the value
    # to the current library
    # if library.id not in library_groups:
    #     library_groups[library.id] = library
    #     library_groups[library.id].books.append(book)

    # If the key does exist, just append the current
    # book to the list of books for the current library
    # else:
    #     library_groups[library.id].books.append(book)


        template = 'employees/employee_list.html'
        context = {
            'employees': employees,
            'roles': roles
        }
        return render(request, template, context)
