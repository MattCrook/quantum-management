from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import SignUpForm
from quantummanagementapp.models import AdminUser, Image
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import error, success, INFO
from rest_framework.authtoken.models import Token


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            # token = Token.objects.create(user=user)
            # admin_user = AdminUser.objects.get(user_id=user.id)
            # new_image = Image()
            # new_image.save()
            # admin_user.image_id = new_image.id
            # admin_user.save()
            login(request, user)
            return redirect(reverse('quantummanagementapp:home'))
        else:
            print(form.errors.as_data())
            messages.add_message(request, messages.ERROR, 'Passwords not match')
            return redirect(reverse('quantummanagementapp:register'))

    else:
        admin_users = AdminUser.objects.all()
        form = SignUpForm()
        template = 'registration/register.html'
        context = {
            'admin_users': admin_users,
            'form': form
        }
        return render(request, template, context)
