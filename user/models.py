from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from polymorphic.models import PolymorphicModel

from common.models import BaseModel, BaseModelWithName


class User(BaseModel, AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    email_confirmed = models.BooleanField(_('Email confirmed'), default=False)
    phone = models.CharField(_('Phone Number'), max_length=10, unique=True)
    phone_confirmed = models.BooleanField(_('Phone confirmed'), default=False)

    @property
    def fullname(self):
        return self.get_full_name() if self.first_name and self.last_name else self.username

    class Meta(AbstractUser.Meta):
        db_table = 'users'

    def __str__(self):
        return self.fullname


class Profile(BaseModel):
    MALE, FEMALE = 'male', 'female'
    GENDER_LIST = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )
    user = models.OneToOneField(User, models.CASCADE, verbose_name=_('User'))
    birth_date = models.DateField(_('Birth Date'), blank=True, null=True)
    gender = models.CharField(_('Gender'), max_length=6, choices=GENDER_LIST, blank=True, null=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profile')

    def __str__(self):
        return self.user.fullname


class Address(BaseModelWithName, PolymorphicModel):
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('User'))
    phone = models.CharField(_('Phone Number'), max_length=10)
    province = models.ForeignKey('location.Province', models.DO_NOTHING, verbose_name=_('Province'))
    district = models.ForeignKey('location.District', models.DO_NOTHING, verbose_name=_('District'))
    description = models.CharField(_('Description'), max_length=160)
    editable = models.BooleanField(_('Is Editable'), default=True, editable=False)

    class Meta:
        db_table = 'addresses'
        ordering = '-id',
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def clean(self):
        if self.province != self.district.province:
            raise ValidationError({'district': _('This district does not match the selected province.')})


class IndividualAddress(Address):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)

    class Meta:
        db_table = 'individual_addresses'
        verbose_name = _('Individual Address')
        verbose_name_plural = _('Individual Addresses')


class CorporateAddress(Address):
    company_name = models.CharField(_('Company Name'), max_length=150)
    tax_room = models.CharField(_('Tax Room'), max_length=100)
    tax_number = models.CharField(_('Tax Number'), max_length=11)

    class Meta:
        db_table = 'corporate_addresses'
        verbose_name = _('Corporate Address')
        verbose_name_plural = _('Corporate Addresses')
