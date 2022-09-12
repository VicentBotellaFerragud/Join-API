from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.

class LoginTest(TestCase):
    def testLogin(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')
        