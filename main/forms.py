from django import forms
from main.models import Post, Comment, Reaction

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})