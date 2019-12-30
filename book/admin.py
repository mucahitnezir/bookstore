from django.contrib import admin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter

from common.admin import BaseModelAdmin
from .models import Category, Book, BookMeta


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin, MPTTModelAdmin):
    list_display = 'name', 'created_at'
    prepopulated_fields = {'slug': ('name',)}
    search_fields = 'name',

    # django-mptt configuration
    mptt_indent_field = 'name'
    mptt_level_indent = 15


class BookMetaAdmin(admin.StackedInline):
    autocomplete_fields = 'translators',
    model = BookMeta

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Book)
class BookAdmin(BaseModelAdmin):
    autocomplete_fields = 'authors', 'categories', 'publisher'
    inlines = BookMetaAdmin,
    list_display = 'name', 'publisher', 'list_price', 'sale_price', 'created_at'
    list_filter = 'publisher', ('categories', TreeRelatedFieldListFilter),
    prepopulated_fields = {'slug': ('name',)}
    search_fields = 'name', 'publisher__name'
