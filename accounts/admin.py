from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'team', 'status_type', 'position')

    fieldsets = UserAdmin.fieldsets + (
        ('Coordonnées', {'fields': ('phone_number',)}),
        ('Fonction', {'fields': ('team', 'status_type', 'position')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Coordonnées', {'fields': ('phone_number',)}),
        ('Fonction', {'fields': ('team', 'status_type', 'position')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
