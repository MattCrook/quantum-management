from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from quantummanagementapp.views.Api import *
from rest_framework.authtoken.views import obtain_auth_token
from quantummanagementapp.views import gmail_authenticate, auth_return




router = routers.DefaultRouter(trailing_slash=False)

router.register(r'parks', ParkData, 'park')
router.register(r'attractions', AttractionData, 'attraction')
router.register(r'employees', EmployeeData, 'employee')
router.register(r'attraction_wait_times', AttractionWaitTimesData, 'attraction_wait_time')
router.register(r'attraction_types', AttractionTypeData, 'attraction_type')
router.register(r'attraction_visitors', AttractionVisitorData, 'attraction_visitor')
router.register(r'visitors', VisitortData, 'visitor')
router.register(r'visitor_checkouts', VisitorCheckoutData, 'visitor_checkout')
router.register(r'employee_attractions', EmployeeAttractionData, 'employee_attraction')
router.register(r'park_attractions', ParkAttractionsData, 'park_attraction')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('social_django.urls', namespace="social")),
    path('gmailAuthenticate', gmail_authenticate, name ='gmail_authenticate'),
    path('oauth2callback', auth_return),
    path('', include('quantummanagementapp.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
