from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView

from market.forms import UniForm, OfferCreation
from market.models import Offer
from users.models import Uni


class MarketListView(ListView):
    template_name = 'market/market.html'
    title = 'Заказы'

    def get_queryset(self):
        offers = Offer.objects.all()
        unis_check = self.request.GET.get('uni_name')
        return offers.filter(user__uni__pk=unis_check) if unis_check else offers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UniForm()
        context['offers'] = self.get_queryset()
        context['unis'] = Uni.objects.all()
        context['form'] = form
        return context


class IndexView(TemplateView):
    template_name = 'market/index.html'

class OfferCreationView(FormView, SuccessMessageMixin):
    template_name = 'market/create_offer.html'
    form_class = OfferCreation
    success_message = 'Вы успешно создали заказ!'
    success_url = reverse_lazy('marketlistview')


    def form_valid(self, form):
        subject, task, price, deadline =  form.cleaned_data['subject'], form.cleaned_data['task'], form.cleaned_data['price'], form.cleaned_data['deadline']
        new_offer = Offer(subj=subject, user=self.request.user, task=task, price=price, deadline=deadline)
        new_offer.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Действия при неверной отправке формы
        return super().form_invalid(form)
