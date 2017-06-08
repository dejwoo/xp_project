from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.api.models import User


class UserTest(APITestCase):
    def test_create_user(self):
        url = reverse('signup')
        data = {'username': 'ExtremTestUser', 'password': 'ExtremTestUserPassword', 'email': 'Extrem@Test.mail',
                'company': 'ExtremTestCompany'}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, data['username'])



    def test_delete_user(self):
        url = reverse('user-list')
        data = {'id': User.objects.filter(username='ExtremTestUser')}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 0)
