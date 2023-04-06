from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from chat.models import Messages, Room


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def checkview(request):
    # name = request.POST.get('name', False)
    # username = request.user.username.POST['name']

    if request.user.is_authenticated:
        room_queryset = Messages.objects.filter(user__username=request.user).values('room').distinct()
        rq = [one['room'] for one in room_queryset]
        return render(request, "chat/test_show.html")
    else:
        print("Not logged in")


class CheckView(ListView):
    model = Messages
    template_name = 'chat/test_show.html'
    title = 'test'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user.username
        return queryset.filter(user__username=user).values('room').distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    #
    # def get_queryset(self):
    #     if request.user.is_authenticated:
    #         room_queryset = Messages.objects.filter(user__username=request.user).values('room').distinct()
    #         rq = [one['room'] for one in room_queryset]
    #         return render(request, "chat/test_show.html")
    #     else:
    #         print("Not logged in")
