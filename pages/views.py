"""
    The app pages stores some utility files:
    - fixtures for the tests
    - base.html
    - home.html
"""

from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


class SecurityInfo(TemplateView):
    template_name = "pages/security_info.html"
