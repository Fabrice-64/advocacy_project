from django.urls import path
import officials.views as views


app_name = "officials"

urlpatterns = [
    path('dispatch/', views.official_dispatch, name="official_dispatch"),
    path('mandate/add/', views.mandate_add, name="mandate_add"),
    path('mandates/add/senator/', views.SenatorMandateCreateView.as_view(), name="add_senator_mandate"),
    path('mandates/add/mp/', views.MPMandateCreateView.as_view(), name="add_mp_mandate"),
    path('mandates/add/region/', views.RegionMandateCreateView.as_view(), name="add_region_mandate"),
    path('mandates/add/department/', views.DepartmentMandateCreateView.as_view(), name="add_department_mandate"),
    path('mandates/add/intercom/', views.IntercomMandateCreateView.as_view(), name="add_intercom_mandate"),
    path('mandates/add/city/', views.CityMandateCreateView.as_view(), name="add_city_mandate"),
    path('list/', views.OfficialListView.as_view(), name="official_list"),
    path('official/details/<uuid:pk>/', views.OfficialDetailView.as_view(), name="official_details"),
    path('official/create/', views.OfficialCreateView.as_view(), name="official_create"),
    path('ajax/load_mandate_city/', views.load_mandate_city, name="ajax_load_mandate_city"),
]