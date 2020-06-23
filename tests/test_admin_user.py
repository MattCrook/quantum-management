# import unittest
from django.test import TestCase
from django.urls import reverse
from quantummanagementapp.models import AdminUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from unittest import skip
import json
import unittest
from django.shortcuts import redirect


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser1",
            password="Test123",
            email="TestUSer1@me.com",
            first_name="Test",
            last_name="User1"
        )


    def test_get(self):
        # Get request for user created in setup
        response = self.client.get(reverse('quantummanagementapp:home'))

        # Checks to make sure get request went through
        self.assertEqual(response.status_code, 302)



if __name__ == '__main__':
    unittest.main()
