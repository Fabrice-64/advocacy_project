from django.contrib.auth import views
from django.urls import path, include
#from .views import SignUpPageView


urlpatterns = [
   path('', include('registration.backends.default.urls')),
]