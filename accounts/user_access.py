"""
    This User Access Mixin is used to check the permissions when
    a user wants to access a view.
    It is used in all applications.
"""

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import PermissionRequiredMixin


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(),
                self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect(reverse_lazy("pages:home"))
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)