from django.urls import path
import pages.views as views

app_name = "pages"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('security-info', views.SecurityInfo.as_view(), name='security_info')
]
