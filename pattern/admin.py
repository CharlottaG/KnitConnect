from django.contrib import admin
from .models import Pattern
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pattern)
class PatternAdmin(SummernoteModelAdmin):

    list_display = ('pattern_name', 'slug', 'status', 'created_on')
    search_fields = ['pattern_name', 'yarn']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('pattern_name',)}
    summernote_fields = ('description',)