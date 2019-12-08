from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('phone', 'email', 'name', 'surname', 'password1', 'password2')
