from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quantummanagementapp.models import AdminUser

@login_required
def index(request):
    if request.method == 'GET':
        user = request.user
        user_data = User.objects.get(username=user)
        user_id = user_data.id
        admin_user = AdminUser.objects.get(user_id=user_id)

        template = 'base.html'
        context = {
            'user': user_data,
            'admin_user': admin_user
            }

        return render(request, template, context)
