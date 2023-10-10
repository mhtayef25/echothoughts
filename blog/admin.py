from django.contrib import admin

from .models import Blog, Category, Comment, Profile, Section

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name']
    search_fields = ['user__first_name__istartswith','user__last_name__istartswith']

    @admin.display(ordering='user__first_name')
    def first_name(self,profile):
        return profile.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self,profile):
        return profile.user.last_name

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title__istartswith']


class SectionInline(admin.StackedInline):
    model = Section
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ['header','author','created_at','update_at']
    autocomplete_fields = ['author','category']
    search_fields = ['header__istartswith']
    list_filter = ['created_at','update_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','commenter','created_at','update_at']
    autocomplete_fields = ['blog','commenter']
