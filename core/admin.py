from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.contrib.contenttypes.admin import GenericTabularInline

from blog.admin import BlogAdmin
from blog.models import Blog
from core.models import User
from tag.models import TaggedItem

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

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 1

class CustomBlogAdmin(BlogAdmin):
    inlines = BlogAdmin.inlines + [TagInline]

admin.site.unregister(Blog)
admin.site.register(Blog,CustomBlogAdmin)