from django.contrib import admin
from market.models import ModelSubject, ModelUni, ModelOfferOrder

# Register your models here.

@admin.register(ModelUni)
class UserAdmin(admin.ModelAdmin):
    list_display = ['uni_name']

@admin.register(ModelSubject)
class UserAdmin(admin.ModelAdmin):
    list_display = ['subj_name']

@admin.register(ModelOfferOrder)
class UserAdmin(admin.ModelAdmin):
    list_display = ['task']
