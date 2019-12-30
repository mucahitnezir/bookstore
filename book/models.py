from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.models import BaseModelWithSlug, BaseModel


class Category(BaseModelWithSlug, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(_('Description'), blank=True, null=True)

    class Meta:
        db_table = 'categories'
        ordering = 'name',
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Book(BaseModelWithSlug):
    authors = models.ManyToManyField('author.Author', verbose_name=_('Authors'))
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'))
    publisher = models.ForeignKey('publisher.Publisher', models.DO_NOTHING, verbose_name=_('Publisher'))
    list_price = models.DecimalField(_('List Price'), max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(_('Sale Price'), max_digits=6, decimal_places=2)
    image = models.ImageField(_('Image'))
    description = models.TextField(_('Description'), blank=True, null=True)
    on_sale = models.BooleanField(_('On Sale'), default=True)

    class Meta:
        db_table = 'books'
        ordering = '-id',
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class BookMeta(BaseModel):
    book = models.OneToOneField(Book, models.CASCADE, verbose_name=_('Book'))
    isbn = models.CharField(_('ISBN'), max_length=13, blank=True, null=True, unique=True)
    number_of_pages = models.IntegerField(_('Number of Pages'), blank=True, null=True)
    number_of_prints = models.IntegerField(_('Number of Prints'), blank=True, null=True)
    release_date = models.DateField(_('Release Date'), blank=True, null=True)
    dimension = models.ForeignKey('shared.Dimension', models.DO_NOTHING, blank=True, null=True, verbose_name=_('Dimension'))
    translators = models.ManyToManyField('author.Translator', blank=True, verbose_name=_('Translators'))

    class Meta:
        db_table = 'book_meta'
        verbose_name = _('Book Meta')
        verbose_name_plural = _('Book Meta')

    def __str__(self):
        return self.book.name
