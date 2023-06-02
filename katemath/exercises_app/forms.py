from django import forms


class AnswerForm(forms.Form):
    """Form for answer to exercise"""
    answer = forms.CharField(max_length=128, label='Odpowiedź: ')
