from django.contrib import admin

# Register your models here.
from chat.models import Room, Messages

@admin.register(Room)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk']
@admin.register(Messages)
class UserAdmin(admin.ModelAdmin):
    list_display = ['value']