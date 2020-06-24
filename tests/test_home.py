from django import urls
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, redirect
import unittest
from django.contrib.auth import authenticate, get_user_model
from django import urls

# Test verify that the site renders as expected
class TestHome(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_quantum_site(self):
        url = urls.reverse('quantummanagementapp:landing_page')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual( b'Quantum Management' in resp.content, 1)


if __name__ == '__main__':
    unittest.main()
