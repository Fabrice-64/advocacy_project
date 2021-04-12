from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phone_number', 'team']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'team',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('phone_number', 'team',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
