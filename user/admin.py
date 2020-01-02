from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from common.admin import BaseModelAdmin
from .models import User, Profile, Address, IndividualAddress, CorporateAddress


class ProfileAdmin(admin.StackedInline):
    model = Profile

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(User)
class UserAdmin(BaseModelAdmin, BaseUserAdmin):
    inlines = ProfileAdmin,
    list_display = 'first_name', 'last_name', 'email', 'phone', 'username', 'is_staff'
    list_filter = 'is_staff', 'is_superuser', 'is_active', 'email_confirmed', 'phone_confirmed', 'groups'
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'email_confirmed', 'phone_confirmed')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class BaseChildAddressModelAdmin(PolymorphicChildModelAdmin):
    base_model = Address


@admin.register(IndividualAddress)
class IndividualProviderAdmin(BaseChildAddressModelAdmin):
    pass


@admin.register(CorporateAddress)
class CorporateAddressAdmin(BaseChildAddressModelAdmin):
    pass


@admin.register(Address)
class ProviderAdmin(BaseModelAdmin, PolymorphicParentModelAdmin):
    base_model = Address
    child_models = (IndividualAddress, CorporateAddress)
    list_display = 'user', 'province', 'district', 'polymorphic_ctype', 'phone'
    search_fields = 'user__first_name', 'user__last_name'
