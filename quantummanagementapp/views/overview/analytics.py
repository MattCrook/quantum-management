from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AttractionVisitors, AttractionWaitTimes, Visitor, VisitorCheckOut, ParkAttractions, Employee, Attraction, AdminUser, Park, ParkAttractions
from django.http import HttpResponseServerError
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def analytics(request, park_id):
    if request.method == 'GET':
        user = request.user
        admin_user = AdminUser.objects.get(user_id=user.id)
        park = Park.objects.get(pk=park_id)
        employees = Employee.objects.filter(park_id=park_id)
        visitors = Visitor.objects.filter(park_id=park_id)
        park_attractions = ParkAttractions.objects.filter(park_id=park_id)
        all_wait_times = AttractionWaitTimes.objects.filter(park_id=park_id)
        visitor_checkouts = VisitorCheckOut.objects.filter(park_id=park_id)
        attractions = Attraction.objects.filter(park_id=park_id)
        attraction_visitors = []

        for attraction in park_attractions:
            attraction_id = attraction.id
            attraction_visit = AttractionVisitors.objects.filter(attraction_id=attraction_id)
            attraction_visitors.append(attraction_visit)

        current_time = datetime.datetime.now()
        count = count_attraction_visitors(attraction_visitors)
        attractions_count = count_attractions(attractions)


        template = 'overview/analytics.html'
        context = {
            'admin_user': admin_user,
            'park': park,
            'employees': employees,
            'visitors': visitors,
            'park_attractions': park_attractions,
            'wait_times': all_wait_times,
            'visitor_checkouts': visitor_checkouts,
            'attraction_visitors': attraction_visitors,
            'attractions': attractions,
            'current_time': current_time,
            'count': count,
            'attractions_count': attractions_count,
        }
        return render(request, template, context)


def count_attraction_visitors(attr_vis):
    attr_vis_arr = []
    for v_array in attr_vis:
        for v in v_array:
            attr_vis_arr.append(v)
    count = len(attr_vis_arr)
    return count

def count_attractions(attr):
    attr_arr = []
    for a in attr:
        attr_arr.append(a)
    count = len(attr_arr)
    return count
