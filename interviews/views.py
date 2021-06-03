"""
    These views deal with the advocacy topics and the interviews.

    As Interviews with the officials should contain sensitive data, 
    the information sharing is strictly controlled: the assessment of
    an interview is exclusively accessible either to the volunteeer
    designated to lead it or to a manager.

    class:
        InterviewAssessmentView
    
    Advocacy Topics are the political guidelines that drive the charity.
    Therefore, their creation is as well strictly controlled: only a manager can update it.

    class: 
       AdvocacyTopicUpdateView

"""
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import AdvocacyTopic, Interview
from .forms import AdvocacyTopicForm, InterviewForm, InterviewAssessmentForm
from accounts.user_access import UserAccessMixin



class AdvocacyTopicListView(UserAccessMixin, ListView):
    permission_required = "interviews.view_advocacytopic"
    model = AdvocacyTopic
    queryset = AdvocacyTopic.objects.order_by('keyword', '-is_active')
    template_name = "advocacy_topics/advocacy_topic_list.html"
    paginate_by =10


class AdvocacyTopicDetailView(UserAccessMixin, DetailView):
    permission_required = "interviews.view_advocacytopic"
    model = AdvocacyTopic
    template_name = "advocacy_topics/advocacy_topic_detail.html"


class AdvocacyTopicCreateView(UserAccessMixin, CreateView):
    permission_required = "interviews.add_advocacytopic"
    model = AdvocacyTopic
    form_class = AdvocacyTopicForm
    template_name = "advocacy_topics/advocacy_topic_create_form.html"
    success_url = reverse_lazy("interviews:advocacy_topic_list")


class AdvocacyTopicUpdateView(UserAccessMixin, UpdateView):
    permission_required = "interviews.change_advocacytopic"
    model = AdvocacyTopic
    form_class = AdvocacyTopicForm
    template_name = "advocacy_topics/advocacy_topic_update_form.html"
    success_url = reverse_lazy("interviews:advocacy_topic_list")
    

class InterviewListView(UserAccessMixin, ListView):
    permission_required = "interviews.view_interview"
    model = Interview
    queryset = Interview.objects.order_by('status', 'date_effective')
    template_name = "interviews/interviews_list.html"
    paginate_by = 10


class InterviewDetailView(UserAccessMixin, DetailView):
    permission_required = "interviews.view_interview"
    model = Interview
    template_name = "interviews/interview_details.html"


class InterviewCreateView(UserAccessMixin, CreateView):
    permission_required = "interviews.add_interview"
    model = Interview
    form_class = InterviewForm
    template_name = "interviews/interview_create_form.html"
    success_url = reverse_lazy("interviews:interviews_list")


class InterviewUpdateView(UserAccessMixin, UpdateView):
    permission_required = "interviews.change_interview"
    model = Interview
    form_class = InterviewForm
    template_name = "interviews/interview_update_form.html"
    success_url = reverse_lazy("interviews:interview_details", args=["uuid"])


class InterviewAssessmentView(UserAccessMixin, UserPassesTestMixin, UpdateView):
    permission_required = "interviews.change_interview"
    model = Interview
    form_class = InterviewAssessmentForm
    template_name = "interviews/interview_assessment_form.html"
    success_url = reverse_lazy("interviews:interview_details", args=["uuid"])

    def test_func(self):
        # Purpose is to grant access exclusively to to the interviewer and managers.
        interview = self.get_object()
        if self.request.user == interview.volunteer or self.request.user.status_type == "MANAGER":
            return True
