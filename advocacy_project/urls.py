"""
    advocacy_project URL Configuration
    All the apps have their initial url being implemented.
    the app pages is used exclusively to deal with base.html and home.html.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('communities/', include('communities.urls')),
    path('interviews/', include('interviews.urls')),
    path('teams/', include('teams.urls')),
    path('officials/', include('officials.urls'))
]
