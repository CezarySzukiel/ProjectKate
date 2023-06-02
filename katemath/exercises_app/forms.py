from django import forms
from .models import Exercises, Sections, Subsections


class AnswerForm(forms.Form):
    """Form for answer to exercise"""
    answer = forms.CharField(max_length=128, label='Odpowiedź: ')


class FilterForm(forms.Form):
    """Form for filtering exercises"""
    sections = forms.ModelMultipleChoiceField(queryset=Sections.objects.all(),
                                              widget=forms.CheckboxSelectMultiple,
                                              required=False)
    subsections = forms.ModelMultipleChoiceField(queryset=Subsections.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple,
                                                 required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subsections'].queryset = Subsections.objects.all()

    def set_subsections_queryset(self, sections_ids):
        self.fields['subsections'].queryset = Subsections.objects.filter(section__in=sections_ids)
        # self.fields['subsections'].initial = Subsections.objects.filter(section__in=sections_ids)
        # self.fields['subsections'].widget.attrs.update({'disabled': 'disabled'})

