"""
    The accounts module mainly makes use of Django generic views.
    However, user registration is managed by django-registration-redux.
    Link to the doc: https://django-registration-redux.readthedocs.io/en/latest/

    Function:
    change_password: used for the first login of a new user.

    These views are closely linked to the custom settings (cf end of the settings after
    REGISTRATION_FORM)
"""
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
# Partial use of django-registration-redux functionalities.
from registration.backends.default.views import RegistrationView
from accounts.user_access import UserAccessMixin
from accounts.models import CustomUser, Volunteer


@login_required
def change_password(request):
    """
        Used in the workflow at first connection of a new user.
        This function implements the Group to which the user belongs.
    """
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Attributes to a user a group depending on his status.
            user.groups.add(Group.objects.get(name=user.status_type))
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Votre mot de passe a été changé')
            return redirect(reverse_lazy('pages:home'))
        else:
            messages.error(request, 'S\'il vous plait, corrigez l\'erreur.')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


def user_types(request):
    """
        This view only display a choice list for the user
        to select the category of people he wants to access to.
    """
    return render(request, "accounts/user_types.html")


class UserRegistrationView(PermissionRequiredMixin, RegistrationView):
    # Keeps the user registration for managers
    permission_required = "accounts.add_customuser"


class VolunteerListView(UserAccessMixin, ListView):
    permission_required = "accounts.view_volunteer"
    # pagination html is displayed in the template base.html
    paginate_by = 20
    model = Volunteer
    # Ordering by teams is used for the grouping in the template
    queryset = Volunteer.objects.order_by("team")


class VolunteerDetailView(UserAccessMixin, DetailView):
    permission_required = "accounts.view_volunteer"
    model = Volunteer
    template_name = "accounts/volunteer_detail.html"
    success_url = reverse_lazy("volunteer_details")


class StaffListView(UserAccessMixin, ListView):
    permission_required = "accounts.view_employee"
    paginate_by = 20
    model = CustomUser
    queryset = CustomUser.objects.filter(Q(status_type="MANAGER") | Q(status_type="EMPLOYEE")).order_by("position")
    template_name = "accounts/staff_list.html"


class StaffDetailView(UserAccessMixin, DetailView):
    permission_required = "accounts.view_employee"
    model = CustomUser
    template_name = "accounts/staff_detail.html"
    success_url = reverse_lazy('staff_details')
