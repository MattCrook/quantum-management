from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import SignUpForm
from quantummanagementapp.models import AdminUser
from django.contrib.auth import login


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('quantummanagementapp:home'))

    elif request.method == 'GET':
        admin_users = AdminUser.objects.all()
        form = SignUpForm()

        template = 'registration/register.html'
        context = {
            'admin_users': admin_users,
            'form': form
        }
        return render(request, template, context)
