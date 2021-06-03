from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from accounts.user_access import UserAccessMixin
from .models import Team
from .forms import TeamForm
# Create your views here.


class TeamListView(ListView):
    paginate_by = 20
    model = Team
    queryset = Team.objects.order_by("-city", "name")


class TeamCreateView(UserAccessMixin, CreateView):
    permission_required = "teams.add_team"
    model = Team
    form_class = TeamForm
    template_name = "teams/team_create_form.html"
    success_url = reverse_lazy("teams:team_list")
