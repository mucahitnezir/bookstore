from django.contrib import admin

from common.admin import BaseModelAdmin
from .models import Publisher


@admin.register(Publisher)
class PublisherAdmin(BaseModelAdmin):
    list_display = 'name', 'slug', 'created_at'
    list_filter = 'created_at',
    prepopulated_fields = {'slug': ('name',)}
    search_fields = 'name',
