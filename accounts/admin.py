from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()
# Customization Admin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'team', 'status_type')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'team', 'status_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('phone_number', 'team', 'status_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
