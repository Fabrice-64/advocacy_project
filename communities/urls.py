from django.urls import path, include
import communities.views as views
from django.contrib.auth.decorators import permission_required

app_name = 'communities'

urlpatterns = [
    path('', views.communities, name='list'),
    path("regions/list/", views.RegionsListView.as_view(), name="region_list")
]