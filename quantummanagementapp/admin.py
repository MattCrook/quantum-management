from django.contrib import admin
from quantummanagementapp.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


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
admin.site.register(Roles)
admin.site.register(CredentialsModel)
# admin.site.register(CustomUserSocialAuth)
# admin.site.register(CustomDjangoStorage)

# admin.site.register(CredentialsAdmin)
