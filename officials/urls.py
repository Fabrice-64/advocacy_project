from django.urls import path
import officials.views as views


app_name = "officials"

urlpatterns = [
    path('pages/', views.official_pages, name="official_pages"),
    path('mandate/list/', views.MandateList.as_view(), name="mandate_list"),
    path('official/list/', views.OfficialList.as_view(), name="official_list")
]