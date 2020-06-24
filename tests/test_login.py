from django.test import TestCase
import unittest
from django.contrib.auth import authenticate, get_user_model
from django.urls import reverse
from django.shortcuts import render, redirect
from quantummanagementapp.models import AdminUser
from django.contrib.auth.models import User
from django import urls


class TestLogin(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', password='12test12', email='test@example.com', first_name='Matt', last_name='Crook')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

def test_redirect_to_home_when_logged_in(self, authenticated_user, client):
    url = urls.reverse('home')
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('quantummanagementapp:home')





if __name__ == '__main__':
    unittest.main()
