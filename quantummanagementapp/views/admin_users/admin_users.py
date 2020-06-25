import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseServerError
from quantummanagementapp.models import AdminUser, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import status


def admin_user_register(request):
    if request.method == 'GET':
        try:
            admin_users = AdminUser.objects.all()
            template = 'admin_users_list.html'
            context = {
                'admin_users': admin_users
            }
            return render(request, template, context)
        except Exception as ex:
            return HttpResponseServerError(ex)

    elif request.method == 'POST':
        try:
            form_data = request.POST
            new_user = User.objects.create_user(
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                username=form_data['username'],
                email=form_data['email'],
            )
            new_admin_user = AdminUser()
            new_admin_user.pictue = form_data['picture'],
            new_admin_user.role = form_data['role'],
            new_admin_user = new_user

            new_admin_user.save()
            return redirect(reverse('quantummanagementapp:home'))
        except Exception as ex:
            return HttpResponseServerError(ex)


@login_required
def get_admin_user_profile(request, user_id):
    if request.method == 'GET':
        user_account = User.objects.get(pk=user_id)
        admin_user_profile = AdminUser.objects.get(user_id=user_account.id)
        employees = Employee.objects.filter(admin_user_id=user_id)
        template = 'admin_user/account.html'
        context = {
            'user_account': user_account,
            'admin_user_profile': admin_user_profile,
            'employees': employees
        }
        return render(request, template, context)


@login_required
def admin_user_edit_form(request, user_id):
    if request.method == 'GET':
        user_account = User.objects.get(pk=user_id)
        admin_user_profile = AdminUser.objects.get(user_id=user_account.id)
        employees = Employee.objects.filter(admin_user_id=user_id)
        template = 'admin_user/admin_user_edit_form.html'
        context = {
            'user_account': user_account,
            'admin_user_profile': admin_user_profile,
            'employees': employees
        }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        if ('actual_method' in form_data and form_data['actual_method'] == 'PUT'):
            user = User.objects.get(pk=user_id)
            admin_user_profile = AdminUser.objects.get(user_id=user.id)
            employees = Employee.objects.filter(admin_user_id=user_id)

            user.first_name = form_data["first_name"]
            user.last_name = form_data["last_name"]
            user.username = form_data["username"]
        # "When Django handles a file upload, the file data ends up placed in request.FILES"
        # https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
            if request.FILES:
                newproduct.image_path = request.FILES["image_path"]

            admin_user_profile.picture = form_data["picture"]
            admin_user_profile.role = form_data["role"]
            user.save()
            admin_user_profile.save()
            return redirect(reverse('quantummanagementapp:account', kwargs={'user_id': user.id}))
