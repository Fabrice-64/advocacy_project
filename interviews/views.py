from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import AdvocacyTopic
from .forms import AdvocacyTopicForm
from accounts.user_access import UserAccessMixin
# Create your views here


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

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
