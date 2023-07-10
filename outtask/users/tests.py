# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from users.models import User
from market.models import Order, Offer, Subject



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

        url = reverse('account_login')
        response = self.client.post(url, data)


        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='abobus')
        self.assertTrue(user.is_authenticated)


class DealMakeTest(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='customer', email='testuser1@example.com',
                                                 password='testpassword')
        self.subj = Subject.objects.create(subj_name='матан')
        self.offer = Offer.objects.create(subj=self.subj, user=self.customer)
        self.order = Order.objects.create(user=self.customer, offer=self.offer)

        self.data = {'pk': self.order.id}

    def test_give_order(self):
        url = reverse('give-order', kwargs=self.data)
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertTrue(self.order.status)


    def test_refuse(self):
        url = reverse('refuse', kwargs=self.data)
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        try:
            self.order.refresh_from_db()
            _ = 0
        except:
            _ = 1

        self.assertTrue(_)


    def test_not_came(self):
        url = reverse('not-ready', kwargs=self.data)
        rating_before = self.customer.rating
        response = self.client.post(url)
        self.customer.refresh_from_db()
        rating_after = self.customer.rating

        self.assertEqual(response.status_code, 302)
        self.assertEqual(rating_before - 1, rating_after)

        try:
            self.offer.refresh_from_db()
            _ = 0
        except:
            _ = 1

        self.assertTrue(_)


    def test_came(self):
        pass

    def test_like(self):
        pass

    def test_neutral(self):
        pass

    def test_dislike(self):
        pass