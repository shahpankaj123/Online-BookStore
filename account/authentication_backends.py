from django.contrib.auth.backends import ModelBackend
from .models import User

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None,):
        user = User.objects.get(email=email)
        if user and user.check_password(password):
            return user
        return None