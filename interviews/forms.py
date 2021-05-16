from django.forms import ModelForm, CharField, TextInput, Form
from .models import AdvocacyTopic


class AdvocacyTopicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quote'].widget.attrs.update({'rows': 2})

    class Meta:
        model = AdvocacyTopic
        fields = ['keyword', 'key_statement', 'source_title', 'source', 'quote', 'is_active']


