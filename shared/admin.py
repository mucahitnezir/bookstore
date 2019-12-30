from django.contrib import admin

from common.admin import BaseModelAdmin
from .models import Country, Dimension, Language


@admin.register(Country)
class CountryAdmin(BaseModelAdmin):
    list_display = 'name',
    search_fields = 'name',


@admin.register(Dimension)
class DimensionAdmin(BaseModelAdmin):
    list_display = 'name',
    search_fields = 'name',


@admin.register(Language)
class LanguageAdmin(BaseModelAdmin):
    list_display = 'name',
    search_fields = 'name',
