# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from users.models import User


class RegistrationLoginTest(TestCase):

    def test_register(self):
        data = {
            'username' : 'abobus',
            'email' : 'soccor@bk.ru',
            'password1' : 'testpassword',
            'password2' : 'testpassword',
        }

        url = reverse('account_signup')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_email_verification_sent'))

        user = User.objects.get(username='abobus')
        self.assertEqual(user.email, 'soccor@bk.ru')
        self.assertTrue(user.check_password('testpassword'))

    def test_login(self):
        User.objects.create_user(username='abobus', email='testuser@example.com', password='testpassword')
        data = {
            'login': 'abobus',
            'password': 'testpassword',
        }

        print(data)

        url = reverse('account_login')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='abobus')
        self.assertTrue(user.is_authenticated)

# Create your tests here.

