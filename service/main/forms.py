from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = HomeNew
        fields = ('time_create', 'content')
        widgets = {
            'time_create': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }