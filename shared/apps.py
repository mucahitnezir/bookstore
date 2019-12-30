from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SharedConfig(AppConfig):
    name = 'shared'
    verbose_name = _('Shared')
