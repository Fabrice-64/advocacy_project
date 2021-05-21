from django.urls import path
import officials.views as views


app_name = "officials"

urlpatterns = [
    path('pages/', views.official_pages, name="official_pages"),
    path('mandate/change/', views.mandate_change, name="mandate_change"),
    path('official/list/', views.official_pages, name="official_list")
]