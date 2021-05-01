from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from communities.models import Region, City, Department, Intercom


def load_intercom(request):
    department_id = request.GET.get('department')
    intercoms = Intercom.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'communities/intercom_dropdown_list.html', 
                    {'intercoms': intercoms})

def communities(request):
    return render(request, "communities/communities.html")

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(),
                self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect(reverse_lazy("pages:home"))
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

class RegionsListView(ListView):
    model = Region


class RegionCreateView(UserAccessMixin, CreateView):
    permission_required = 'communities.add_region'
    model = Region
    fields = ['name']
    template_name="communities/region_create_form.html"
    success_url = reverse_lazy("communities:region_create")


class DepartmentListView(ListView):
    model = Department

from communities.forms import DepartmentForm
class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name="communities/department_create_form.html"
    success_url = reverse_lazy("communities:department_list")
    
class IntercomListView(ListView):
    model = Intercom

from communities import forms as forms
class IntercomCreateView(CreateView):
    model = Intercom
    form_class = forms.IntercomForm
    template_name="communities/intercom_create_form.html"
    success_url = reverse_lazy("communities:intercom_list")


class CityListView(ListView):
    model = City

from communities import forms as forms
class CityCreateView(CreateView):
    model = City
    form_class = forms.CityForm
    template_name="communities/city_create_form.html"
    success_url = reverse_lazy("communities:city_list")