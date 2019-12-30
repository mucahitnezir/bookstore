from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

UserModel = get_user_model()


class EmailBackend(BaseBackend):
    """
    Custom authentication backend, via email
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password) and getattr(user, 'is_active', None) is True:
                return user
            return
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
