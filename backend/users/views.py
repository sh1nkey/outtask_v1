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


class Profile(TitleMixin, TemplateView):
    template_name = 'users/profile.html'
    title = 'Профиль'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  LoginChangeForm
        context['username'] = self.request.user.username
        context['form1'] = UniUpdateForm
        context['uni_name'] = self.request.user.uni
        context['offers'] = UsersOffersListView.get_queryset(self)
        context['taken_offers'] = UsersOrdersListView.get_queryset(self)
        context['rating'] = self.request.user.rating
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


class UsersOffersListView(ListView):

    def get_queryset(self):
        offers = Offer.objects.filter(user=self.request.user)
        return  offers

class UsersOrdersListView(ListView):

    def get_queryset(self):
        taken_offers_id = Order.objects.filter(user=self.request.user).values_list('offer', flat=True)
        taken_offers=Offer.objects.filter(id__in=taken_offers_id)
        return  taken_offers


class DeleteOffers(DeleteView):
    model = Offer
    success_url = reverse_lazy('profile')


class DeleteOrders(DeleteView):
    model = Order
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.model.objects.get(offer__id=self.kwargs.get('pk'))






