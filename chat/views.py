from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from chat.models import Messages, Room


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def checkview(request):
    # name = request.POST.get('name', False)
    # username = request.user.username.POST['name']

    if request.user.is_authenticated:
        print(f"Logged in as {request.user}")
        room_queryset = Messages.objects.filter(user__username=request.user).values('room').distinct()
        rq = [one['room'] for one in room_queryset]
        return HttpResponse(f'{ rq }')
    else:
        print("Not logged in")
