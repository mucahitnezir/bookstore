from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel


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


class Address(BaseModel):
    INDIVIDUAL, CORPORATE = 'individual', 'corporate'
    TYPE_LIST = (
        (INDIVIDUAL, _('Individual')),
        (CORPORATE, _('Corporate')),
    )
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('User'))
    province = models.ForeignKey('location.Province', models.DO_NOTHING, verbose_name=_('Province'))
    district = models.ForeignKey('location.District', models.DO_NOTHING, verbose_name=_('District'))
    zip_code = models.CharField(_('Zip Code'), max_length=6)
    description = models.CharField(_('Description'), max_length=160)
    type = models.CharField(_('Type'), max_length=10, choices=TYPE_LIST, default=INDIVIDUAL)
    tax_room = models.CharField(_('Tax Room'), max_length=100, blank=True, null=True)
    tax_number = models.CharField(_('Tax Number'), max_length=11, blank=True, null=True)
    editable = models.BooleanField(_('Is Editable'), default=True, editable=False)

    class Meta:
        db_table = 'addresses'
        ordering = '-id',
        verbose_name = _('Address')
        verbose_name_plural = _('Address')

    def __str__(self):
        return str(self.user)

    def clean(self):
        if self.province != self.district.province:
            raise ValidationError({'district': _('This district does not match the selected province.')})
        if self.type == self.CORPORATE:
            if not self.tax_room:
                raise ValidationError({'tax_room': _('Tax room is required for corporate addresses.')})
            if not self.tax_number:
                raise ValidationError({'tax_number': _('Tax number is required for corporate addresses.')})
