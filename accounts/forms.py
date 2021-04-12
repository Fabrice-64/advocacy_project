
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from registration.forms import RegistrationForm

class CustomUserCreationForm(RegistrationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone_number', 'team')



class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'phone_number', 'team')
