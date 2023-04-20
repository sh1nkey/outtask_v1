from django.contrib.messages.views import SuccessMessageMixin
from django.core import paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, FormView, DeleteView

from market.forms import  UniForm
from market.models import Offer, Order

from users.forms import LoginChangeForm, UniUpdateForm
from users.models import User

from common.views import TitleMixin

from users.forms import LinkChangeForm


class Profile(TitleMixin, TemplateView):
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  LoginChangeForm
        context['username'] = self.request.user.username
        context['form1'] = UniUpdateForm
        context['uni_name'] = self.request.user.uni
        context['rating'] = self.request.user.rating
        context['form2'] = LinkChangeForm
        context['socnet'] = self.request.user.socnet_link
        return context


class LoginUpdate(SuccessMessageMixin, UpdateView):
    model = User
    form_class = LoginChangeForm
    success_message = 'Логин успешно изменен!'
    success_url = reverse_lazy('profile')

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy('profile'))


class VUZUpdate(SuccessMessageMixin, FormView):
    form_class = UniForm
    success_message = 'ВУЗ изменен успешно!'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        new_uni = form.cleaned_data['uni_name']
        user = self.request.user
        user.uni = new_uni
        user.save()
        return super().form_valid(form)


class LinkUpdate(SuccessMessageMixin, FormView):
    form_class = LinkChangeForm
    success_message = 'Ссылка на ваш аккаунт соц.сети установлена!'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        socnet_link = form.cleaned_data['socnet_link']
        user = self.request.user
        user.socnet_link = socnet_link
        user.save()
        return super().form_valid(form)


class PerCabView(TitleMixin, TemplateView):
    template_name = 'users/personal_cabinet.html'
    title = 'Личный кабинет'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = UsersOffersListView.get_queryset(self)
        context['taken_offers'] = UsersOrdersListView.get_queryset(self)
        context['taken_orders'] = TakersOrdersListView.get_queryset(self)
        return context


class UsersOffersListView(ListView):

    def get_queryset(self):
        offers = Offer.objects.filter(user=self.request.user)
        return  offers


class UsersOrdersListView(ListView):

    def get_queryset(self):
        taken_offers_id = Order.objects.filter(user=self.request.user).values_list('offer', flat=True)
        taken_offers=Offer.objects.filter(id__in=taken_offers_id)
        return  taken_offers


class TakersOrdersListView(ListView):

    def get_queryset(self):
        taken_orders = Order.objects.filter(offer__user=self.request.user)
        return  taken_orders


class DeleteOffers(DeleteView):
    model = Offer
    success_url = reverse_lazy('personal_cabinet')


class DeleteOrders(DeleteView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')

    def get_object(self, queryset=None):
        return self.model.objects.get(offer__id=self.kwargs.get('pk'))


class GiveOrder(SuccessMessageMixin, FormView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')
    success_message = 'Заказ успешно отдан!'

    def post(self, request, *args, **kwargs):
        change_status = self.model.objects.get(pk=self.kwargs.get('pk'))
        offer_of_order = change_status.offer.pk
        if change_status.status == 0:
            change_status.status = 1
            change_status.save()
            delete_orders = Order.objects.filter(status=0, offer__pk=offer_of_order)
            delete_orders.delete()
        return HttpResponseRedirect(reverse_lazy('personal_cabinet'))


class RefuseOrder(SuccessMessageMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.kwargs.get('pk'))


class OrderReady(SuccessMessageMixin, FormView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')
    success_message = 'Заказ успешно отдан!'

    def post(self, request, *args, **kwargs):
        change_status = self.model.objects.get(pk=self.kwargs.get('pk'))
        if change_status.status == 1:
            change_status.status = 2
            change_status.save()
        return HttpResponseRedirect(reverse_lazy('personal_cabinet'))


class NotHereOrder(FormView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')

    def post(self, request, *args, **kwargs):
        ord = Order.objects.get(pk=self.kwargs.get('pk'))
        user = ord.user
        user.rating -= 1
        user.save()
        ord.offer.delete()
        return HttpResponseRedirect(reverse_lazy('personal_cabinet'))

class LikeView(SuccessMessageMixin, FormView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')
    success_message = 'Рейтинг исполнителя повышен!!'

    def post(self, request, *args, **kwargs):
        print(kwargs.get('pk'))
        working_order = self.model.objects.get(pk=self.kwargs.get('pk'))
        print(working_order)
        working_order.user.rating += 1
        working_order.user.save()
        working_order.offer.delete()
        return HttpResponseRedirect(reverse_lazy('personal_cabinet'))

class NeutralView(FormView):
    model = Order
    success_url = reverse_lazy('personal_cabinet')

    def post(self, request, *args, **kwargs):
        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return HttpResponseRedirect(reverse_lazy('personal_cabinet'))




