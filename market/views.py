from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView, FormView
from django.views.generic.edit import FormMixin, DeleteView, UpdateView

from market.forms import UniForm, OfferCreation
from market.models import Offer
from users.models import Uni, User


class MarketListView(ListView):
    template_name = 'market/market.html'
    title = 'Заказы'

    def get_queryset(self):
        offers = Offer.objects.all()
        unis_check = self.request.GET.get('uni_name')
        offers.filter(deadline__lt=now()).delete()
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


class OfferCreationView(FormView):
    template_name = 'market/create_offer.html'
    form_class = OfferCreation
    success_url = reverse_lazy('markett')

    def form_valid(self, form):
        subject, task, price, deadline = form.cleaned_data['subject'], form.cleaned_data['task'], form.cleaned_data[
            'price'], form.cleaned_data['deadline']
        new_offer = Offer(subj=subject, user=self.request.user, task=task, price=price, deadline=deadline)
        new_offer.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class OfferDelete(SuccessMessageMixin, DeleteView):
    model = Offer
    success_url = reverse_lazy('profile')
    template_name = 'market/profile.html'
    success_message = 'Заказ успешно удалён!'
