from django.test import TestCase
from django.urls import reverse

from market.models import Subject, Offer, Order
from users.models import User
from django.utils import timezone


# class MarketTest(TestCase):
#     def setUp(self):
#         self.customer = User.objects.create_user(username='customer', email='testuser1@example.com',
#                                                  password='testpassword')
#         self.worker = User.objects.create_user(username='worker', email='testuser2@example.com',
#                                                password='testpassword')
#         self.subj = Subject.objects.create(subj_name='матан')
#
#     def test_offer_create(self):
#
#         # пишем текст в формы
#         # отправляем его
#         # проверяем, создалось ли предложение
#
#
#         self.client.login(username='customer', password='testpassword')
#
#         data = {
#             'subject' : self.subj.id,
#             'task' : 'протестируй мне сайт',
#             'price' : 100,
#             'deadline' : timezone.localdate()
#         }
#
#
#         url = reverse('createoffer')
#         response = self.client.post(url,  data=data)
#         self.assertEqual(response.status_code, 302)




'''
создать заказ
взять заказ
'''