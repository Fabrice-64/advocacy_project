from django.urls import path, include
import communities.views as views
from django.contrib.auth.decorators import permission_required

app_name = 'communities'

urlpatterns = [
    path('', views.community_types, name='list'),
    path("region/list/", views.RegionsListView.as_view(), name="region_list"),
    path("region/create/", views.RegionCreateView.as_view(), name="region_create"),
    path("department/list/", views.DepartmentListView.as_view(), name="department_list"),
    path("department/create/", views.DepartmentCreateView.as_view(), name="department_create"),
    path("intercom/list/", views.IntercomListView.as_view(), name="intercom_list"),
    path("intercom/create/", views.IntercomCreateView.as_view(), name="intercom_create"),
    path("city/list/", views.CityListView.as_view(), name="city_list"),
    path("city/create/", views.CityCreateView.as_view(), name="city_create"),
    path('ajax/load_departments/', views.load_department, name="ajax_load_departments"),
]