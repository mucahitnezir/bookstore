from django.contrib import admin

from common.admin import BaseModelAdmin
from .models import Province, District


@admin.register(Province)
class ProvinceAdmin(BaseModelAdmin):
    list_display = 'name',
    prepopulated_fields = {'slug': ('name',)}
    search_fields = 'name',


@admin.register(District)
class DistrictAdmin(BaseModelAdmin):
    list_display = 'name', 'province'
    list_filter = 'province',
    prepopulated_fields = {'slug': ('name',)}
    search_fields = 'name',
