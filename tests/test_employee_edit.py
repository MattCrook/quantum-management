from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, redirect
from quantummanagementapp.models import AdminUser, Park, Employee
from django.contrib.auth.models import User
import unittest
from django.contrib.auth import authenticate, get_user_model
from django import urls


class TestEditEmployee(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def testGetCustomer(self):
    #     self.createCustomer()

    #     response = self.client.get(
    #         '/customers'
    #     )

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]["id"], 1)
    #     self.assertEqual(response.data[0]["address"], "111 test road")

    # def testEditCustomer(self):
    #     self.createCustomer()

    #     updated_customer = {
    #         "address": "New Address",
    #         "phone_number": "4455555555"
    #     }

    #     response = self.client.put(
    #         reverse('customer-detail', kwargs={'pk': 1}),
    #         updated_customer,
    #         content_type="application/json",
    #         HTTP_AUTHORIZATION='Token ' + str(self.token_1)
    #     )

    #     self.assertEqual(response.status_code, 204)

    #     response = self.client.get(
    #         reverse('customer-detail', kwargs={'pk': 1}),
    #         HTTP_AUTHORIZATION='Token ' + str(self.token_1)
    #     )

    #     self.assertEqual(response.data["phone_number"], updated_customer["phone_number"])


if __name__ == '__main__':
    unittest.main()
