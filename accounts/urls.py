from django.urls import path, include
from .views import change_password


urlpatterns = [
    path('', include('registration.backends.default.urls'), name="registration"),
    path('change_password/', change_password, name='change_password'),
]