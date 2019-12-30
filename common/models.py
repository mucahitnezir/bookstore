from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True, null=True)

    class Meta:
        abstract = True


class BaseModelWithName(BaseModel):
    name = models.CharField(_('Name'), max_length=150)

    class Meta:
        abstract = True
        ordering = 'name',

    def __str__(self):
        return self.name


class BaseModelWithSlug(BaseModelWithName):
    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        abstract = True
        ordering = 'name',
