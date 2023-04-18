from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView, FormView
from market.forms import UniForm, OfferCreation
from market.models import Offer, Order
from users.models import Uni, User

from common.views import TitleMixin

from backend.market.forms import FilterForm


class MarketListView(TitleMixin, ListView):
    template_name = 'market/market.html'
    title = 'Заказы'
    paginate_by = 10

    def get_queryset(self):
        offers = Offer.objects.all()
        unis_check = self.request.GET.get('uni_name')
        if  unis_check == '':
            unis_check = None
        subj_check = self.request.GET.get('subj_name')
        if  subj_check == '':
            subj_check = None
        offers.filter(deadline__lt=now()).delete()
        if self.request.user.id:
            users_taken_offers = list(Order.objects.filter(user=self.request.user).values_list('offer_id', flat=True))
            offers = offers.exclude(id__in=users_taken_offers)
        if (unis_check is not None) and (subj_check is None):
            return offers.filter(user__uni__pk=unis_check) if unis_check else offers
        elif (subj_check is not None) and (unis_check is None):
            return offers.filter(subj_id=subj_check)
        elif (unis_check and subj_check) is not None:
            return offers.filter(subj_id=subj_check, user__uni__pk=unis_check)
        else:
            return offers

        return offers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = self.get_queryset()
        context['unis'] = Uni.objects.all()
        context['form'] = FilterForm()



        paginator = Paginator(context['offers'], self.paginate_by)
        page = self.request.GET.get('page')

        try:
            my_models = paginator.page(page)
        except PageNotAnInteger:
            my_models = paginator.page(1)
        except EmptyPage:
            my_models = paginator.page(paginator.num_pages)

        context['my_models'] = my_models
        return context


class IndexView(TitleMixin,  TemplateView):
    template_name = 'market/index.html'
    title = 'Главная страница'


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
        if not Order.objects.filter(offer=offer).exists():
            order = Order.objects.create(user=user, offer=offer)
            order.save()
            return redirect(self.success_url)


