from django.shortcuts import render, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django_oso.auth import authorize


# Create your views here.
from communities.models import Region, City, Department, Intercom

def communities(request):
    return render(request, "communities/communities.html")

class RegionsListView(ListView):
    model = Region

    def get_queryset(self):
        return Region.objects.authorize(self.request, action="read")

class RegionCreateView(CreateView):
    model = Region
    fields = ['name']
    template_name="communities/region_create_form.html"
    success_url = "/communities/region/list/"


class DepartmentListView(ListView):
    model = Department

from communities.forms import DepartmentForm
class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name="communities/department_create_form.html"
    success_url = "/communities/department/list/"
    
class IntercomListView(ListView):
    model = Intercom

from communities import forms as forms
class IntercomCreateView(CreateView):
    model = Intercom
    form_class = forms.IntercomForm
    template_name="communities/intercom_create_form.html"
    success_url = "/communities/intercom/list/"


class CityListView(ListView):
    model = City

from communities import forms as forms
class CityCreateView(CreateView):
    model = City
    form_class = forms.CityForm
    template_name="communities/city_create_form.html"
    success_url = "/communities/city/list/"