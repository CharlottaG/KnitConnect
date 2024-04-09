from django.contrib import admin
from .models import User
from django_summernote.admin import SummernoteModelAdmin


@admin.register(User)
class UserAdmin(SummernoteModelAdmin):

    list_display = ['username',]
    search_fields = ['username']
    summernote_fields = ('bio',)