from django.forms import ModelForm, CharField, TextInput, Form
from .models import AdvocacyTopic


class AdvocacyTopicForm(ModelForm):
    class Meta:
        model = AdvocacyTopic
        fields = ['keyword', 'key_statement', 'source_title', 'source', 'quote', 'is_active']


