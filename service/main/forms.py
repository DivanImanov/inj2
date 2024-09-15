from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = HomeNew
        fields = ('time_create', 'content')
        widgets = {
            'time_create': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

class ContactForm(forms.Form):
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Text', 'style':'width: 600px; max-width:96vw;', }))