from django import forms
from .models import Profile, Notes

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user', 'about_yourself', 'media']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})

        self.fields['media'].widget = forms.FileInput(attrs={'class': "form-control"})

class NoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ["title", 'description']

