from django.contrib import admin
from .models import UserReg

# Register your models here.
@admin.register(UserReg)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "password")