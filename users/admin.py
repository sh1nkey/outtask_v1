from django.contrib import admin

# Register your models here.
from users.models import User, Uni


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']

@admin.register(Uni)
class UserAdmin(admin.ModelAdmin):
    list_display = ['uni_name']
