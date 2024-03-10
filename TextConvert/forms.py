# forms.py

from django import forms

class TextAreaForm(forms.Form):
    text_area = forms.CharField(widget=forms.Textarea)
