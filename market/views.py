from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView, FormView
from django.views.generic.edit import FormMixin

from market.forms import UniForm, OfferCreation, LoginChangeForm
from market.models import Offer
from users.models import Uni


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


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



class ProfileView(SuccessMessageMixin, FormView, FormMixin,):
    form_class = LoginChangeForm
    second_form_class = UniForm
    template_name = 'market/profile.html'
    success_message = 'Изменения прошли успешно!!'
    success_url = reverse_lazy('profile')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginChangeForm
        context['email'] = self.request.user.email
        context['username'] = self.request.user.username
        context['uni_name'] = self.request.user.uni
        context['form1'] = UniForm
        return context

    def form_valid(self, form):
        new_username = form.cleaned_data['username']
        user = self.request.user
        user.username = new_username
        user.save()
        return super().form_valid(form)

    def second_form_valid(self, form):
        new_uni = form.cleaned_data['uni_name']
        user = self.request.user
        user.uni = new_uni
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_second_form(self, form_class=None):
        if form_class is None:
            form_class = self.second_form_class
        return form_class(**self.get_form_kwargs())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        second_form = self.get_second_form()
        if form.is_valid():
            return self.form_valid(form)
        elif second_form.is_valid():
            return self.second_form_valid(second_form)
        else:
            return self.form_invalid(form)


# class VuzChangeView(SuccessMessageMixin, FormView):
#     form_class = UniForm
#     template_name = 'market/profile.html'
#     success_message = 'ВУЗ успешно изменен!'
#     success_url = reverse_lazy('profile')
#
#     def form_valid(self, form):
#         new_uni = form.cleaned_data['uni_name']
#         user = self.request.user
#         user.uni.uni_name = new_uni
#         user.save()
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form1'] = UniForm
#         return context
# #
# #
