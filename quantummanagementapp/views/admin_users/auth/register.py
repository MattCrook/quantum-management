# import json
# from django.http import HttpResponse
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from django.views.decorators.csrf import csrf_exempt
# from quantummanagementapp.models import AdminUser


# @csrf_exempt
# def register_user(request):
#     req_body = json.loads(request.body.decode())
#     try:
#         new_user = User.objects.create_user(
#             username=req_body['username'],
#             email=req_body['email'],
#             password=req_body['password'],
#             first_name=req_body['first_name'],
#             last_name=req_body['last_name']
#         )

#         adminUser = AdminUser.objects.create(
#             user=new_user,
#             picture=req_body['picture'],
#             role=req_body['role']
#         )
#         adminUser.save()
#         token = Token.objects.create(user=new_user)
#         data = json.dumps({"token": token.key})
#         return HttpResponse(data, content_type='application/json')

#     except Exception as x:
#         return HttpResponse(x, content_type='application/json')
