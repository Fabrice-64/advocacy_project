"""
    The app pages stores some utility files:
    - fixtures for the tests
    - base.html
    - home.html
"""

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"