from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from accounts.models import CustomUser
from registration.views import RegistrationView
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, login_required, PasswordResetDoneView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Attributes to a user a group depending on his status.
            user.groups.add(Group.objects.get(name=user.status_type))
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form})


from registration.backends.default.views import RegistrationView
class UserRegistrationView(PermissionRequiredMixin, RegistrationView): 
    permission_required = "accounts.add_customuser"
    success_url = reverse_lazy('accounts:registration_activate')



from registration.views import ActivationView
class UserActivationView(RegistrationView):
    pass
