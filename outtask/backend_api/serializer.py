from rest_framework import serializers
from market.models import Subject, Offer
from users.models import Uni


class SubjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subj_name']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['subj', 'task',  'price', 'deadline']


class UniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uni
        fields = ['uni_name']