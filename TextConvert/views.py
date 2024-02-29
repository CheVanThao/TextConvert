from django.shortcuts import render
from django import forms

def homePage(request):
    return render(request, "Home.html")

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)