from django import forms

from res_system.models import Room

class SearchForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control me-2',
            'type': 'search',
            'placeholder': "Type here..."
        }
    ))