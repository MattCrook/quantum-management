from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, redirect
from quantummanagementapp.models import AdminUser, Park, Employee
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from unittest import skip
import json
import unittest
from django.contrib.auth import authenticate, get_user_model


class TestEmployee(TestCase):

    def createPark(self):
        Park.objects.create(name="TestPark", state="Tennessee", max_capacity="10000", number_of_attractions=20)

    def createAdminUser(self):
        AdminUser.objects.create(picture="matt-crook.jpg", role="CEO", user_id=1)

    def createEmployee(self):
        Employee.objects.create(
            first_name="Matt",
            last_name="Crook",
            role="Ride Operator",
            start_date="2020-06-20",
            admin_user_id=1,
            park_id=1,
            pay_rate="salary",
            compensation="40000"
            )


    def setUp(self):
        self.username = "TestUser"
        self.password = "testword1"
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        # self.token = Token.objects.create(user=self.user)

    def test_list_employees(self):
        self.createPark()
        self.createAdminUser()
        new_employee = self.createEmployee()

        response = self.client.get(reverse('quantummanagementapp:employee_list'))
        print("Response", response.content)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(response.data), 1)
        self.assertIn(new_employee.name.encode(), response.content)
