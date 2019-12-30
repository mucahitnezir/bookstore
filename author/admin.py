from django.contrib import admin

from common.admin import BaseModelAdmin
from .models import Author, Translator


@admin.register(Author)
class AuthorAdmin(BaseModelAdmin):
    list_display = 'name', 'country', 'slug', 'created_at'
    list_filter = 'created_at',
    prepopulated_fields = {'slug': ('name',)}
    search_fields = 'name',


@admin.register(Translator)
class TranslatorAdmin(BaseModelAdmin):
    list_display = 'author', 'language_names'
    list_filter = 'languages',
    search_fields = 'author__name',
