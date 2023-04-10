from django.contrib import admin
from market.models import  Subject, Offer



# Register your models here.


@admin.register(Subject)
class UserAdmin(admin.ModelAdmin):
    list_display = ['subj_name']

@admin.register(Offer)
class UserAdmin(admin.ModelAdmin):
    list_display = ['task']

# @admin.register(Order)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['deadline']
