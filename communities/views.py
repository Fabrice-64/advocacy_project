from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from communities.models import Region, City, Department, Intercom
from communities import forms as forms
from accounts.user_access import UserAccessMixin


def load_department(request):
    region_id = request.GET.get('region')
    departments = Department.objects.filter(region_id=region_id).order_by('name')
    return render(
        request, 'communities/department_dropdown_list.html',
        {'departments': departments})


def load_intercom(request):
    department_id = request.GET.get('department')
    intercoms = Intercom.objects.filter(
        department_id=department_id).order_by('name')
    return render(
        request, 'communities/intercom_dropdown_list.html',
        {'intercoms': intercoms})


def load_city(request):
    department_id = request.GET.get('department')
    cities = City.objects.filter(department_id=department_id).order_by('name')
    return render(
        request, 'communities/city_dropdown_list.html',
        {'cities': cities})


def community_types(request):
    """
        Solely used for displaying the types of communities
        the user has access to.
    """
    return render(request, "communities/communities.html")


class RegionsListView(ListView):
    # pagination snippet is written in base.html.
    paginate_by = 10
    model = Region


class RegionCreateView(UserAccessMixin, CreateView):
    permission_required = 'communities.add_region'
    model = Region
    form_class = forms.RegionForm
    template_name = "communities/region_create_form.html"
    success_url = reverse_lazy("communities:region_list")


class DepartmentListView(ListView):
    # pagination snippet is written in base.html.
    paginate_by = 20
    model = Department


class DepartmentCreateView(UserAccessMixin, CreateView):
    permission_required = "communities.add_department"
    model = Department
    form_class = forms.DepartmentForm
    template_name = "communities/department_create_form.html"
    success_url = reverse_lazy("communities:department_list")


class IntercomListView(ListView):
    # pagination snippet is written in base.html.
    paginate_by = 20
    model = Intercom


class IntercomCreateView(UserAccessMixin, CreateView):
    permission_required = "communities.add_intercom"
    model = Intercom
    form_class = forms.IntercomForm
    template_name = "communities/intercom_create_form.html"
    success_url = reverse_lazy("communities:intercom_list")


class CityListView(ListView):
    # pagination snippet is written in base.html.
    paginate_by = 20
    model = City


class CityCreateView(UserAccessMixin, CreateView):
    permission_required = "communities.add_city"
    model = City
    form_class = forms.CityForm
    template_name = "communities/city_create_form.html"
    success_url = reverse_lazy("communities:city_list")
