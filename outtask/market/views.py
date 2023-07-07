from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView, FormView
from market.forms import OfferCreation
from market.models import Offer, Order
from users.models import Uni
from django.db.models import Q
from common.views import TitleMixin
from market.forms import FilterForm

from outtask import settings


class MarketListView(TitleMixin, ListView): # главный view страницы "рынок", который выводит всю информацию и таблицы
    template_name = 'market/market.html'
    title = 'Рынок'
    paginate_by = 5

    def get_queryset(self):
        offers = Offer.objects.all()
        unis_check = self.request.GET.get('uni_name')
        subj_check = self.request.GET.get('subj_name')
        newness_check = self.request.GET.get('newness')

        unis_check = None if unis_check == '' else unis_check
        subj_check = None if subj_check == '' else subj_check
        offers.filter(deadline__lt=now()).delete()  # удаляет просроченные заказы
        if self.request.user.id:
            users_taken_offers = list(Order.objects.filter(user=self.request.user).values_list('offer_id', flat=True))
            offers = offers.exclude(id__in=users_taken_offers)

        filter_Q = Q()  # создание сложного запроса: проверка трех независимых условий
        if unis_check is not None:
            filter_Q &= Q(user__uni__pk=unis_check)
        if subj_check is not None:
            filter_Q &= Q(subj_id=subj_check)
        return offers.filter(filter_Q).order_by('-date_create') if newness_check else offers.filter(filter_Q)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = self.get_queryset()
        context['unis'] = Uni.objects.all()
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['form'] = FilterForm()

        paginator = Paginator(context['offers'], self.paginate_by) # отсюда в этой функции начинается логика пагинации
        page = self.request.GET.get('page')

        try:
            my_models = paginator.page(page)
        except PageNotAnInteger:
            my_models = paginator.page(1)
        except EmptyPage:
            my_models = paginator.page(paginator.num_pages)

        context['my_models'] = my_models
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'market/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        print(settings.MEDIA_URL)
        return context


class OfferCreationView(TitleMixin, FormView):
    template_name = 'market/create_offer.html'
    title = 'Создать заказ'
    form_class = OfferCreation
    success_url = reverse_lazy('markett')

    def form_valid(self, form):
        subject, task, price, deadline = form.cleaned_data['subject'], form.cleaned_data['task'], form.cleaned_data[
            'price'], form.cleaned_data['deadline']
        new_offer = Offer(subj=subject, user=self.request.user, task=task, price=price, deadline=deadline)
        new_offer.save()
        return super().form_valid(form)


class OrderAdd(SuccessMessageMixin, FormView):
    model = Order
    success_url = reverse_lazy('markett')
    success_message = 'Заказ успешно добавлен!'

    def post(self, request, *args, **kwargs):
        user = self.request.user
        offer = Offer.objects.get(pk=self.kwargs['pk'])
        if not Order.objects.filter(offer=offer, user=user).exists(): # чтобы юзер случайно не создал два заказа с помощью дабл-клика
            order = Order.objects.create(user=user, offer=offer)
            order.save()
        return redirect(self.success_url)


