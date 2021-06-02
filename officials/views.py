from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
import officials.models as models
import officials.forms as forms
from officials.calculations import calculate_ranking
from officials.ranking_statistics import GetStatsFromOfficials
from accounts.user_access import UserAccessMixin
from interviews.models import Interview


@login_required
@permission_required("officials.view_official", login_url='login/')
def official_dispatch(request):
    return render(request, "officials/officials_dispatch.html")

@login_required
@permission_required("officials.view_official", login_url='login/')
def mandate_add(request):
    return render(request, "mandates/mandate_add.html")

class SenatorMandateCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_senatormandate"
    model = models.SenatorMandate
    fields = ['department', 'start_year']
    template_name = "mandates/senator_mandate_form.html"
    success_url = reverse_lazy("officials:mandate_add")

class MPMandateCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_mpmandate"
    model = models.MPMandate
    fields = ['department', 'start_year']
    template_name = "mandates/mp_mandate_form.html"
    success_url = reverse_lazy("officials:mandate_add")

class RegionMandateCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_mandateregion"
    model = models.MandateRegion
    fields = ['region', 'start_year', 'function']
    template_name = "mandates/region_mandate_form.html"
    success_url = reverse_lazy("officials:mandate_add")

class DepartmentMandateCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_mandatedepartment"
    model = models.MandateDepartment
    fields = ['department', 'start_year', 'function']
    template_name = "mandates/department_mandate_form.html"
    success_url = reverse_lazy("officials:mandate_add")


class IntercomMandateCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_mandateintercom"
    model = models.MandateInterCom
    form_class = forms.MandateInterComForm
    template_name="mandates/intercom_mandate_form.html"
    success_url = reverse_lazy("officials:mandate_add")

class CityMandateCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_mandatecity"
    model = models.MandateCity
    form_class = forms.MandateCityForm
    template_name="mandates/city_mandate_form.html"
    success_url = reverse_lazy("officials:mandate_add")


class OfficialListView(UserAccessMixin, ListView):
    permission_required = "officials.view_official"
    model = models.Official
    queryset = models.Official.objects.order_by('last_name', 'first_name')
    template_name = "officials/official_list.html"
    paginate_by =10


class OfficialDetailView(UserAccessMixin, DetailView):
    permission_required = "officials.view_official"
    model = models.Official
    template_name = "officials/official_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.official = self.get_object()
        context["interviews"] = Interview.objects.filter(official=self.official.id).order_by("date_planned")
        return context
    

class OfficialCreateView(UserAccessMixin, CreateView):
    permission_required = "officials.add_official"
    model = models.Official
    form_class = forms.OfficialCreationForm
    template_name = "officials/official_create_form.html"
    success_url = reverse_lazy("officials:official_dispatch")


@login_required
@permission_required("officials.view_official", login_url='login/')
def official_ranking(request):
    officials = models.Official.objects.all()
    officials_ranking = calculate_ranking(officials)
    officials_categories = GetStatsFromOfficials(officials_ranking)
    context = dict()
    context["little_proximity_high_influence"] = officials_categories.get_officials_below_P50_above_I50()
    context["high_proximity_high_influence"] = officials_categories.get_officials_above_P50_above_I50()
    context["high_proximity_little_influence"] = officials_categories.get_officials_above_P50_below_I50()
    context["little_proximity_little_influence"] = officials_categories.get_officials_below_P50_I50()
    return render(request, "officials/officials_ranking.html", context)
