from django.contrib import admin
from .models import LoginUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(LoginUser)
class LoginUserAdmin(UserAdmin):
    fieldsets =  UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )