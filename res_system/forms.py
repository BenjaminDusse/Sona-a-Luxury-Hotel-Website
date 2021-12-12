from django import forms

from res_system.models import Room, Subscribers, MailMessage


class SearchForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'search-input',
            'type': 'text',
            'placeholder': "Search here.....",

        }
    ))


class SubscribersForm(forms.ModelForm):
    email = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Email',
            }
        ))

    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    
    class Meta:
        model = MailMessage
        fields = '__all__'