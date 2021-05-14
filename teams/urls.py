from django.urls import path
from .views import TeamListView, TeamCreateView

app_name = 'teams'

urlpatterns = [
    path('team/list/', TeamListView.as_view(), name='team_list'),
    path('team/create/', TeamCreateView.as_view(), name='team_create'),
]