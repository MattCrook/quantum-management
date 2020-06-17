import json
from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseServerError
from quantummanagementapp.models import AdminUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required
def list(request):
    if request.method == 'GET':
        try:
            admin_users = AdminUser.objects.all()
            template = 'admin_users_list.html'
            context = {
                'admin_users': admin_users
            }
            return render(request, template, context)
        except Exception as ex:
            return HttpResponseServerError(ex)

    elif request.method == 'POST':
        form_data = request.POST
        print("FORMDATA", form_data)
        # user_id = request.user.id
        new_user = User.objects.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            username=form_data['username'],
            email=form_data['email'],
        )
        new_admin_user = AdminUser.objects.create(
            pictue=form_data['picture'],
            role=form_data['role'],
            # user_id=user_id,
            user=new_user
        )
        new_admin_user.save()

        return redirect(reverse('quantummangementapp:home'))



# class AdminUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = AdminUser
        # url = serializers.HyperlinkedIdentityField(
        #     view_name='adminUser',
        #     lookup_field='id'
        # )
        # fields = ('id', 'picture', 'role', 'user_id', 'user',)
        # depth = 1
        # extra_kwargs = {'password': {'write_only': True}}

    # class AdminUsers(ViewSet):

    #     def list(self, request):
    #         try:
    #             admin_users = AdminUser.objects.all()
        # serializer = AdminUserSerializer(admin_users, many=True, context={'request': request})
        # template = 'home.html'
        # context = {
        #     'admin_users': admin_users
        # }
        # return render(request, template, context)
        # return Response(serializer.data)
        # except Exception as ex:
        #     return HttpResponseServerError(ex)
