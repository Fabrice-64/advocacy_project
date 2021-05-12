from django.urls import path, include
import interviews.views as views
from django.contrib.auth.decorators import permission_required

app_name = 'interviews'

urlpatterns = [
    path("advocacy_topic/list/", views.AdvocacyTopicListView.as_view(), name="advocacy_topic_list"),
    #path("reference/create/", views.ReferenceCreateView.as_view(), name="reference_create"),
    #path("advocacy_topic/details/", views.AdvocacyTopicDetailView.as_view(), name="reference_details"),
]