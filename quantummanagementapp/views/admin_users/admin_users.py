import json
from django.shortcuts import render, redirect, reverse
# from django.http import HttpResponse
# from django.http import HttpResponseServerError
from quantummanagementapp.models import AdminUser, Employee, Image, ImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.core.files.base import ContentFile



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
        form = ImageForm()
        admin_user_image_id = admin_user_profile.image_id

        if admin_user_image_id:
            image = Image.objects.get(pk=admin_user_image_id)
            template = 'admin_user/admin_user_edit_form.html'
            context = {
                'user_account': user_account,
                'admin_user_profile': admin_user_profile,
                'employees': employees,
                'form': form,
                'image': image
            }
            return render(request, template, context)

        else:
            template = 'admin_user/admin_user_edit_form.html'
            context = {
                'user_account': user_account,
                'admin_user_profile': admin_user_profile,
                'employees': employees,
                'form': form,
            }
            return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        if ('actual_method' in form_data and form_data['actual_method'] == 'PUT'):
            user = User.objects.get(pk=user_id)
            admin_user_profile = AdminUser.objects.get(user_id=user.id)
            employees = Employee.objects.filter(admin_user_id=user_id)
            image_id = admin_user_profile.image_id

            if request.FILES:
                image = ImageForm(request.POST, request.FILES)
                img_obj = image.instance
                img_obj.image = request.FILES["image"]
                image.save()

            user.first_name = form_data["first_name"]
            user.last_name = form_data["last_name"]
            user.username = form_data["username"]
            admin_user_profile.role = form_data["role"]

            user.save()
            admin_user_profile.save()

        return redirect(reverse('quantummanagementapp:account', kwargs={'user_id': user.id}))




# def admin_user_register(request):
#     print("ADMINUSERREGISETR", request)
#     if request.method == 'GET':
#         try:
#             admin_users = AdminUser.objects.all()
#             template = 'admin_users_list.html'
#             context = {
#                 'admin_users': admin_users
#             }
#             return render(request, template, context)
#         except Exception as ex:
#             return HttpResponseServerError(ex)

#     elif request.method == 'POST':
#         try:
#             form_data = request.POST
#             print("FORMDATA", form_data)
#             new_user = User.objects.create_user(
#                 first_name=form_data['first_name'],
#                 last_name=form_data['last_name'],
#                 username=form_data['username'],
#                 email=form_data['email'],
#             )
#             new_admin_user = AdminUser()
#             new_admin_user.pictue = form_data['picture'],
#             new_admin_user.role = form_data['role'],
#             new_admin_user = new_user

#             new_admin_user.save()
#             return redirect(reverse('quantummanagementapp:home'))
#         except Exception as ex:
#             return HttpResponseServerError(ex)
