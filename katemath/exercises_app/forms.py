from django import forms
from .models import Exercises, Sections, Subsections


class AnswerForm(forms.Form):
    """Form for answer to exercise"""
    answer = forms.CharField(max_length=128, label='Odpowiedź: ')


class FilterForm(forms.Form):
    """Form for filtering exercises"""
    sections_choices = Sections.objects.all()
    subsections_choices = Subsections.objects.all()
    sections = forms.ModelMultipleChoiceField(queryset=sections_choices, widget=forms.CheckboxSelectMultiple)
    subsections = forms.ModelMultipleChoiceField(queryset=subsections_choices, widget=forms.CheckboxSelectMultiple)

