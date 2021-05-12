from django.shortcuts import render
from django.views.generic import ListView
from .models import AdvocacyTopic
# Create your views here.


class AdvocacyTopicListView(ListView):
    model = AdvocacyTopic
    template_name = "advocacy_topics/advocacy_topic_list.html"
    paginate_by =20