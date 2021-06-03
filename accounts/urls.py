"""
    The authentication workflow uses the third party package "django-registration-redux".
    However its implementation has been customized to implement a workflow where the account
    is created by a manager and the future user receives a single usage link in order to activate
    his account.

    As a consequence:
    app_name is not to be used as it creates a bug in this very workflow.
    The following path order prevents the registration.backend to take over the customized views.
    The implemented backend deviates from django-registration-redux normal use. It should remain as
    such in order to avoid those additional bugs.
"""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as views

# In opposition to Dango recommendations
# app_name="accounts" should not be used

urlpatterns = [
    # User administration views
    path('new_user/', views.UserRegistrationView.as_view(), name="new_user"),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name="accounts/logout.html"), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name="accounts/login.html"), name='login'),
    # django-registration-redux should be located here in order to allow the workflow to run.
    path('register/', include('registration.backends.default.urls'), name="registration_register"),
    # User management views
    path('user_types/', views.user_types, name="user_types"),
    path('volunteer/list/', views.VolunteerListView.as_view(), name='volunteer_list'),
    path('volunteer/detail/<uuid:pk>/', views.VolunteerDetailView.as_view(), name='volunteer_details'),
    path('staff/list/', views.StaffListView.as_view(), name="staff_list"),
    path('staff/detail/<uuid:pk>/', views.StaffDetailView.as_view(), name='staff_details'),
    ]
