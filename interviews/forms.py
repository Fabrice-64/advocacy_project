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
        self.fields['volunteer'].widget.attrs.update({'required': 'true'})

    class Meta:
        model = Interview
        fields = ['date_planned', 'official', 'volunteer', 'topics', 'goal', 'status', 'comments']
        widgets = {
            'date_planned': forms.DateInput(attrs={'type': 'date'}),
            'goal': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
            'topics': forms.CheckboxSelectMultiple(),
            'comments': forms.Textarea(attrs={'rows': 2, 'cols': 40})
        }
        help_texts = {'topics': '<p>Cliquez sur les cases qui vous semblent pertinentes</p>'}


class InterviewAssessmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topics'].widget.attrs.update({'readonly': 'readonly'})

    class Meta:
        model = Interview
        fields = ['status', 'date_effective', 'topics', 'outcome', 'assessment', 'comments']
        widgets = {
            'topics': forms.CheckboxSelectMultiple(),
            'date_effective': forms.DateInput(attrs={'type': 'date'}),
            'outcome': forms.Textarea(attrs={
                'rows': 2, 'cols': 40,
                'placeholder': "Ajoutez ici les résultats de l'entretien"}),
            'comments': forms.Textarea(attrs={
                'rows': 2, 'cols': 40,
                'placeholder': "Ajoutez ici votre évaluation de l'entretien"}),
        }
        help_text = {
            'outcome': "<br>Un résultat positif est un engagement clair de l'Elu.",
            'comments': "<br>Permettent de préciser le degré d'atteinte de l'objectif"
        }
