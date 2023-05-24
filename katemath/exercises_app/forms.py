from django import forms

from exercises_app.models import *


class SortForm(forms.Form):
    SORT_CHOICES = (
        ('number', 'Numer'),
        ('subsections', 'Podrozdział'),
        ('sections', 'Rozdział'),
    )
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, label='Sortuj po: ')


class SortBySubsectionsForm(forms.Form):
    subsection = forms.ModelChoiceField(queryset=Subsections.objects.all(), label='Podrozdział: ')


class SortBySectionsForm(forms.Form):
    section = forms.ModelChoiceField(queryset=Sections.objects.all(), label='Rozdział: ')
