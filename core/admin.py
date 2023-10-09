from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser

from core.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUser):
    add_fieldsets = (
        (('Personal info'), {'classes': ('wide',),'fields': ('first_name', 'last_name')}),
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )