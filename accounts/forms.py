
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'team', 'status_type')


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'team', 'status_type')
