from django.forms import ModelForm, CharField, TextInput, Form
from .models import AdvocacyTopic, Interview


class AdvocacyTopicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quote'].widget.attrs.update({'rows': 2})

    class Meta:
        model = AdvocacyTopic
        fields = ['keyword', 'key_statement', 'source_title', 'source', 'quote', 'is_active']


class InterviewForm(ModelForm):

    class Meta:
        model = Interview
        fields = ['volunteer', 'official', 'status', 'date_planned', 'goal', 'topics',\
            'outcome', 'assessment', 'comments'
        ]

