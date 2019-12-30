from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = _('Book')

    def ready(self):
        import book.signals
