from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModelWithSlug


class Publisher(BaseModelWithSlug):
    image = models.ImageField(_('Image'), blank=True, null=True)

    class Meta:
        db_table = 'publishers'
        ordering = 'name',
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

    def get_absolute_url(self):
        return reverse('publisher:detail', kwargs={'slug': self.slug})
