from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from registration.backends.default.views import RegistrationView
from accounts.models import Volunteer
from accounts.user_access import UserAccessMixin


@login_required
def change_password(request):
    """
        Used in the workflow at first connection of a new user.
        This function implements the Group to which the user belongs.
    """
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Attributes to a user a group depending on his status.
            user.groups.add(Group.objects.get(name=user.status_type))
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Votre mot de passe a été changé')
            return redirect('change_password')
        else:
            messages.error(request, 'S\'il vous plait, corrigez l\'erreur.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


class UserRegistrationView(PermissionRequiredMixin, RegistrationView): 
    # Keeps the user registration for managers
    permission_required = "accounts.add_customuser"


class VolunteerListView(UserAccessMixin, ListView):
    permission_required = "accounts.view_volunteer"
    paginate_by = 20
    model = Volunteer


class VolunteerDetailView(DetailView):
    pass

class EmployeeListView(ListView):
    pass

class EmployeeDetailView(DetailView):
    pass
