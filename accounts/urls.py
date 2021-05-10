from django.urls import path, include
from . import views as views
from django.contrib.auth import views as auth_views

#app_name="accounts"

urlpatterns = [
    # User administration views
    path('new_user/', views.UserRegistrationView.as_view(), name="new_user"),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name="accounts/logout.html"), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name="accounts/login.html"), name='login'),
    path('register/', include('registration.backends.default.urls'), name="registration_register"),
    # User management views
    path('user_types/', views.user_types, name="user_types"),
    path('volunteer/list/', views.VolunteerListView.as_view(), name='volunteer_list'),
    path('volunteer_detail/<uuid:pk>/', views.VolunteerDetailView.as_view(), name='volunteer_detail'),
]