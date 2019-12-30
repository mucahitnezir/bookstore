from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthorConfig(AppConfig):
    name = 'author'
    verbose_name = _('Author')
