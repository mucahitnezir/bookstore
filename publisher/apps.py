from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PublisherConfig(AppConfig):
    name = 'publisher'
    verbose_name = _('Publisher')
