from django import forms
from main.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'media']

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["media", "content"]
        widgets = {
            "media": forms.FileInput()
        }