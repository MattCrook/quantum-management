from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import AttractionVisitors, AttractionWaitTimes, Visitor, VisitorCheckOut, ParkAttractions, Employee, Attraction, AdminUser, Park, ParkAttractions
from django.http import HttpResponseServerError
from django.contrib.auth.decorators import login_required


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
        


        # num_of_attractions = count_attractions(attractions)
        # employee_count = count_employees(employees)
        # earnings = total_earnings(visitors)
        # sum_earnings = sum(earnings, 0)
        # total_visitors = len(earnings)

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
            # 'num_of_attractions': num_of_attractions,
            # 'employee_count': employee_count,
            # 'sum_earnings': sum_earnings,
            # 'total_visitors': total_visitors,
        }
        return render(request, template, context)
