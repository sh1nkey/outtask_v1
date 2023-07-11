from django.test import TestCase
from django.urls import reverse
from users.models import User
from market.models import Order, Offer, Subject

'''
Please launch tests individually, like that:

python manage.py test users
python manage.py test market

otherwise strange bug will appear and tests won't work
'''


class RegistrationLoginTest(TestCase):

    def test_register(self):
        data = {
            'username': 'abobus',
            'email': 'soccor@bk.ru',
            'password1': 'testpassword',
            'password2': 'testpassword',
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


'''Dang next testing class is kinda long, but actually:

table element deletion 4/6 (optimized)
comparing rating 2/6
changing status 2/6

i think it's useless to make those tests shorter in volume
'''


class DealMakeTest(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='customer', email='testuser1@example.com',
                                                 password='testpassword')
        self.worker = User.objects.create_user(username='worker', email='testuser2@example.com',
                                               password='testpassword')
        self.subj = Subject.objects.create(subj_name='матан')
        self.offer = Offer.objects.create(subj=self.subj, user=self.customer)
        self.order = Order.objects.create(user=self.worker, offer=self.offer)

        self.data = {'pk': self.order.id}


    def test_refuse(self):
        url = reverse('refuse', kwargs=self.data)
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())

    def test_not_came(self):
        url = reverse('not-ready', kwargs=self.data)
        rating_before = self.worker.rating
        response = self.client.post(url)
        self.worker.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(rating_before - 1, self.worker.rating)

        self.assertFalse(Offer.objects.filter(id=self.offer.id).exists())

    def test_came(self):
        self.order.status = 1
        self.order.save()
        url = reverse('ready', kwargs=self.data)
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 2)

    def test_like(self):
        rating_old = self.worker.rating
        url = reverse('like', kwargs=self.data)
        response = self.client.post(url)
        self.worker.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(rating_old, self.worker.rating - 1)
        self.assertFalse(Offer.objects.filter(id=self.offer.id).exists())

    def test_neutral(self):
        url = reverse('neutral', kwargs=self.data)
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Offer.objects.filter(id=self.offer.id).exists())



class DeleteTest(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='customer', email='testuser1@example.com',
                                                 password='testpassword')
        self.worker = User.objects.create_user(username='worker', email='testuser2@example.com',
                                               password='testpassword')
        self.subj = Subject.objects.create(subj_name='матан')
        self.offer = Offer.objects.create(subj=self.subj, user=self.customer)
        self.order = Order.objects.create(user=self.worker, offer=self.offer)


    def test_offer_delete(self):
        url = reverse('deleteoffer', kwargs={'pk' : self.offer.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Offer.objects.filter(id=self.offer.id).exists())


    def test_order_delete(self):
        url = reverse('deleteorder', kwargs={'pk': self.order.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())



