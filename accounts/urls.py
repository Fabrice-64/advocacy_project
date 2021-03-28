from django.contrib.auth import views
from django.urls import path

app_name =  'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', views.LogoutView.as_view(
        template_name='registration/logout.html'
    ), name='logout'),
]