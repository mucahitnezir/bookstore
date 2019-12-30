from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModelWithSlug, BaseModel


class Author(BaseModelWithSlug):
    country = models.ForeignKey('shared.Country', models.DO_NOTHING, verbose_name=_('Country'), blank=True, null=True)
    image = models.ImageField(_('Image'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)

    class Meta:
        db_table = 'authors'
        ordering = 'name',
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Translator(BaseModel):
    author = models.ForeignKey(Author, models.CASCADE, verbose_name=_('Author'))
    languages = models.ManyToManyField('shared.Language', verbose_name=_('Languages'))

    @property
    def language_names(self):
        languages = self.languages.all()
        return ', '.join([str(language) for language in languages])

    language_names.fget.short_description = _('Languages')

    class Meta:
        db_table = 'translators'
        ordering = 'author__name',
        verbose_name = _('Translator')
        verbose_name_plural = _('Translators')

    def __str__(self):
        return self.author.name
