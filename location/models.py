from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel, BaseModelWithSlug


class Province(BaseModelWithSlug):
    class Meta:
        db_table = 'provinces'
        ordering = 'name',
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')


class District(BaseModelWithSlug):
    province = models.ForeignKey(Province, models.CASCADE, verbose_name=_('Province'))

    class Meta:
        db_table = 'districts'
        ordering = 'province', 'name',
        verbose_name = _('District')
        verbose_name_plural = _('Districts')
