from django.contrib.auth.models import AbstractUser
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
