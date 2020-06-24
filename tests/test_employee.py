from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, redirect
from quantummanagementapp.models import AdminUser, Park, Employee
from django.contrib.auth.models import User
import unittest
from django.contrib.auth import authenticate, get_user_model
from django import urls


class TestEmployee(TestCase):

    def setUp(self):
        self.username = "TestUser"
        self.password = "testword1"
        self.user = User.objects.create_user(
            username=self.username, password=self.password)

    def tearDown(self):
        pass

    def createPark(self):
        Park.objects.create(name="TestPark", state="Tennessee",
                            max_capacity="10000", number_of_attractions=20)


    def createEmployee(self):
        Employee.objects.create(
            first_name="Tester",
            last_name="Employee",
            role="Ride Operator",
            start_date="2020-06-20",
            admin_user_id=1,
            park_id=1,
            pay_rate="salary",
            compensation="40000"
        )

    def test_list_employees(self):
        new_employee = self.createEmployee()
        new_park = self.createPark()

        response = self.client.get(reverse('quantummanagementapp:employee_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(b'Matt' in response.content, 0)
