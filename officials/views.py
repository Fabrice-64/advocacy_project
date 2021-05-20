from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import officials.models as models
from accounts.user_access import UserAccessMixin
from django.contrib.auth.mixins import UserPassesTestMixin

def official_pages(request):
    return render(request, "officials/officials_pages.html")

class OfficialList(ListView):
    model = models.Official
    queryset = models.Official.objects.order_by("last_name")
    template_name = "officials/official_list.html"
    paginate_by = 10

class MandateList(ListView):
    model = models.MPMandate
    queryset = models.MPMandate.objects.order_by("department", "start_date")
    template_name = "officials/mandates_list.html"
    paginate_by = 10

