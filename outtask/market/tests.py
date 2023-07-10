from django.test import TestCase
from django.urls import reverse

from market.models import Subject, Offer, Order
from users.models import User
from django.utils import timezone


class MarketTest(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='customer', email='testuser1@example.com',
                                                 password='testpassword')
        self.worker = User.objects.create_user(username='worker', email='testuser2@example.com',
                                               password='testpassword')
        self.subj = Subject.objects.create(subj_name='матан')

    def test_offer_create(self):
        self.client.login(username='customer', password='testpassword')

        data = {
            'subject' : self.subj.id,
            'task' : 'протестируй мне сайт',
            'price' : 100,
            'deadline' : timezone.localdate()
        }

        self.assertFalse(len(Offer.objects.all()))
        url = reverse('createoffer')
        response = self.client.post(url,  data=data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(len(Offer.objects.all()))


    def test_take_order(self):
        self.client.login(username='customer', password='testpassword')

        offer = Offer.objects.create(subj=self.subj, user=self.customer, task='lmao test', price=1, deadline=timezone.localdate())
        data = {'pk' : offer.id}

        url = reverse('addoffer', kwargs=data)
        response = self.client.post(url, data=data)


        self.assertEqual(response.status_code, 302)
        self.assertTrue(len(Order.objects.all()))

