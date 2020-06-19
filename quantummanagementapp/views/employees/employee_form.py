from quantummanagementapp.models import Employee
from django.shortcuts import render, redirect, reverse
import datetime
from django.contrib.auth.decorators import login_required
from quantummanagementapp.models import Employee
from django import forms

@login_required
def employee_form(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        template = "employees/employee_form.html"
        context = {
            'employees': employees
        }
        return render(request, template, context)

@login_required
def employee_edit_form(request, pk=None):
    if request.method == 'GET':
        employee = Employee.objects.get(pk=pk)
        template = "employees/employee_form.html"
        context = {
            'employee': employee
        }
        return render(request, template, context)
