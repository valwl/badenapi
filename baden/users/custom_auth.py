from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None,  **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                phone_number = User.objects.phone_normalise(username)
                user = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

