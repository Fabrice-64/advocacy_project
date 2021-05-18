from django.forms import ModelForm, CharField, TextInput, Form
from .models import AdvocacyTopic, Interview
from django import forms

class AdvocacyTopicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quote'].widget.attrs.update({'rows': 2})

    class Meta:
        model = AdvocacyTopic
        fields = ['keyword', 'key_statement', 'source_title', 'source', 'quote', 'is_active']


class InterviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['official'].widget.attrs.update({'required': 'true'})
        self.fields['volunteer'].widget.attrs.update({'required': 'ture'})


    class Meta:
        model = Interview
        fields = ['date_planned', 'official', 'volunteer', 'topics', 'goal', 'status', 'comments']
        widgets = {
            'date_planned': forms.DateInput(attrs={'type': 'date'}),
            'goal': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'topics': forms.CheckboxSelectMultiple()
            }
        help_texts = {'topics': '<p>Sélection Multiple: clic + ctrl pour PC, clic + cmd pour Mac</p>'}
    


