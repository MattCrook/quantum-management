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
        template = 'employees/employee_list.html'
        context = {
            'employees': employees
        }
        return render(request, template, context)
