from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from django.views.generic.edit import UpdateView, FormView

from market.forms import  UniForm
from market.models import Offer
from users.forms import LoginChangeForm, UniUpdateForm

from users.models import User


class Profile(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_update'] = LoginUpdate.as_view()(self.request, pk=self.request.user.pk)
        context['form'] =  LoginChangeForm
        context['username'] = self.request.user.username
        context['vuz_update'] = VUZUpdate.as_view()
        context['form1'] = UniUpdateForm
        context['uni_name'] = self.request.user.uni
        offers = UsersOffersListView.get_queryset(self)
        context['offers'] = offers
        print(context['offers'])
        return context


class LoginUpdate(SuccessMessageMixin, UpdateView):
    model = User
    form_class = LoginChangeForm
    template_name = 'users/profile.html'
    success_message = 'Логин успешно изменен!'
    success_url = reverse_lazy('profile')


class VUZUpdate(SuccessMessageMixin, FormView):
    form_class = UniForm
    template_name = 'market/profile.html'
    success_message = 'ВУЗ изменен успешно!'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        new_uni = form.cleaned_data['uni_name']
        user = self.request.user
        user.uni = new_uni
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UsersOffersListView(ListView):
    template_name = 'market/market.html'
    title = 'Заказы'

    def get_queryset(self):
        offers = Offer.objects.filter(user=self.request.user)
        return  offers


