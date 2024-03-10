from django.shortcuts import render
from django import forms
from .models import Post
from .forms import TextAreaForm

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    
    
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'your_app/post_list.html', {'posts': posts})


def home(request):
    if request.method == 'POST':
        form = TextAreaForm(request.POST)
        if form.is_valid():
            text_data = form.cleaned_data['text_area']
            # Do something with the text data, like saving to database
            print(text_data)
    else:
        form = TextAreaForm()
    return render(request, 'Home.html', {'form': form})