from django.urls import path
import officials.views as views


app_name = "officials"

urlpatterns = [
    path('pages/', views.official_pages, name="official_pages"),
    path('mandate/add/', views.mandate_add, name="mandate_add"),
    path('official/list/', views.official_pages, name="official_list"),
    path('mandates/add/senator/', views.SenatorMandateCreateView.as_view(), name="add_senator_mandate"),
    path('mandates/add/mp/', views.MPMandateCreateView.as_view(), name="add_mp_mandate"),
    path('mandates/add/region/', views.RegionMandateCreateView.as_view(), name="add_region_mandate"),
    path('mandates/add/department/', views.DepartmentMandateCreateView.as_view(), name="add_department_mandate")
]