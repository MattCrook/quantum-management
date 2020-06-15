from django.contrib import admin
from quantummanagementapp.models import AdminUser, Attraction, AttractionType, AttractionWaitTimes, AttractionVisitors, Employee, EmployeeAttraction, Visitor, VisitorCheckOut, Park, ParkAttractions
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(AdminUser)
admin.site.register(Attraction)
admin.site.register(AttractionType)
admin.site.register(AttractionWaitTimes)
admin.site.register(Employee)
admin.site.register(AttractionVisitors)
admin.site.register(EmployeeAttraction)
admin.site.register(Visitor)
admin.site.register(VisitorCheckOut)
admin.site.register(Park)
admin.site.register(ParkAttractions)
