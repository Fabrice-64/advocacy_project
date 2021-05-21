from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import officials.models as models
from accounts.user_access import UserAccessMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("officials.view_official", login_url='login/')
def official_pages(request):
    return render(request, "officials/officials_pages.html")

@login_required
@permission_required("officials.view_official", login_url='login/')
def mandate_change(request):
    return render(request, "mandates/mandate_change.html")

class OfficialList(ListView):
    model = models.Official
    queryset = models.Official.objects.order_by("last_name")
    template_name = "officials/official_list.html"
    paginate_by = 10


