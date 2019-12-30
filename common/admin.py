from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class BaseModelAdmin(admin.ModelAdmin):
    list_display_links = ('get_action_buttons',)

    def __init__(self, model, admin_site):
        self.list_display = ('id', *self.list_display, 'get_action_buttons')
        super().__init__(model, admin_site)

    def get_action_buttons(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name
        return format_html(
            '<a href="{}" class="button action-button">{}</a>',
            reverse("admin:%s_%s_change" % (app_label, model_name), args=[obj.id]),
            _('Detail')
        )

    get_action_buttons.short_description = _('Actions')
