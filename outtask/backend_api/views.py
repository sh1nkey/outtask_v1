from django.shortcuts import render
from rest_framework.views import APIView
from market.models import Subject, Offer
from users.models import Uni
from .serializer import SubjSerializer, UniSerializer, OfferSerializer
from rest_framework  import response

class MarketRestView(APIView):
    def get(self, request):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers,  many=True)
        return response.Response(serializer.data)

