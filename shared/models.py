from django.utils.translation import ugettext_lazy as _

from common.models import BaseModelWithName


class Country(BaseModelWithName):
    class Meta:
        db_table = 'rel_countries'
        ordering = 'name',
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Dimension(BaseModelWithName):
    class Meta:
        db_table = 'rel_dimensions'
        ordering = 'name',
        verbose_name = _('Dimension')
        verbose_name_plural = _('Dimensions')


class Language(BaseModelWithName):
    class Meta:
        db_table = 'rel_languages'
        ordering = 'name',
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
