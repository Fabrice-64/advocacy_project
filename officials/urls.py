from django.urls import path
import officials.views as views


app_name = "officials"

urlpatterns = [
    path('pages/', views.official_pages, name="official_pages"),
    path('mandate/add/', views.mandate_add, name="mandate_add"),
    path('official/list/', views.official_pages, name="official_list"),
    path('mandates/add/senator/', views.SenatorMandateCreateView.as_view(), name="add_senator_mandate")
]