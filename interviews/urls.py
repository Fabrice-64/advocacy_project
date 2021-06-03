from django.urls import path, include
import interviews.views as views


app_name = 'interviews'

urlpatterns = [
    path("advocacy_topic/list/", views.AdvocacyTopicListView.as_view(), name="advocacy_topic_list"),
    path("advocacy_topic/create/", views.AdvocacyTopicCreateView.as_view(), name="advocacy_topic_create"),
    path("advocacy_topic/details/<slug>/", views.AdvocacyTopicDetailView.as_view(), name="advocacy_topic_detail"),
    path("advocacy_topic/update/<slug>/", views.AdvocacyTopicUpdateView.as_view(), name="advocacy_topic_update"),
    path("interview/list/", views.InterviewListView.as_view(), name="interviews_list"),
    path("interview/details/<uuid:pk>/", views.InterviewDetailView.as_view(), name="interview_details"),
    path("interview/create/", views.InterviewCreateView.as_view(), name="interview_create"),
    path("interview/update/<uuid:pk>/", views.InterviewUpdateView.as_view(), name="interview_update"),
    path("interview/assessment/<uuid:pk>/", views.InterviewAssessmentView.as_view(), name="interview_assessment")
]
