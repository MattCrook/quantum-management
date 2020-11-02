from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AdminUser, Attraction, AttractionVisitors, Park, ParkAttractions
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
# from django.contrib.sessions.base_session import AbstractBaseSession, BaseSessionManager



@login_required
def add_attraction_visitor(request, park_id):
    if request.method == 'GET':
        session = request.session.session_key
        user = request.user
        attractions = Attraction.objects.filter(park_id=park_id)
        # session_user = AdminUser.objects.get(session=user)
        token = Token.objects.get(user_id=user.id)
        park = Park.objects.get(pk=park_id)
        template = 'attractions/add_attraction_visitor.html'
        context = {
            'user': user,
            'attractions': attractions,
            'park': park,
        }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        print(form_data)
        new_visitor = AttractionVisitors()
        new_visitor.visit_timestamp = form_data['visit_timestamp']
        new_visitor.attraction_id = form_data['attraction_id']
        new_visitor.save()
        return redirect(reverse('quantummanagementapp:analytics', kwargs={'park_id': park_id}))
