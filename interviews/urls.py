from django.urls import path, include
import interviews.views as views
from django.contrib.auth.decorators import permission_required

app_name = 'interviews'

urlpatterns = [
    path("advocacy_topic/list/", views.AdvocacyTopicListView.as_view(), name="advocacy_topic_list"),
    path("advocacy_topic/create/", views.AdvocacyTopicCreateView.as_view(), name="advocacy_topic_create"),
    path("advocacy_topic/details/<slug>/", views.AdvocacyTopicDetailView.as_view(), name="advocacy_topic_detail"),
    path("advocacy_topic/update/<slug>/", views.AdvocacyTopicUpdateView.as_view(), name="advocacy_topic_update")
]