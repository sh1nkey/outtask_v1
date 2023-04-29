from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from market.models import Subject, Offer
from users.models import Uni
from .serializer import SubjSerializer, UniSerializer, OfferSerializer
from rest_framework.response  import Response

class MarketRestView(APIView):
    def get(self, request):
        output = [
            {
                "subj" : output.subj.subj_name,
                "task" : output.task,
                "price" : output.price,
                "deadline" : output.deadline
            } for output in Offer.objects.all()
        ]

        print(output)
        return Response(output)

