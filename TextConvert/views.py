from django.shortcuts import render
from django import forms
from .models import Post

def homePage(request):
    return render(request, "Home.html")

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    
    
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'your_app/post_list.html', {'posts': posts})