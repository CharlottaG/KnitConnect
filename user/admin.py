from django.contrib import admin
from .models import User
from django_summernote.admin import SummernoteModelAdmin


@admin.register(User)
class UserAdmin(SummernoteModelAdmin):

    list_display = ('username', 'slug')
    search_fields = ['username']
    prepopulated_fields = {'slug': ('username',)}
    summernote_fields = ('bio',)