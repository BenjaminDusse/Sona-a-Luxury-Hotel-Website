from django import forms

from res_system.models import Room, Subscribers, MailMessage


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
    name = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Your Name',
            }
        ))
    email = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Your Email',
            }
        ))
    message = forms.CharField(
        required=True,
        max_length=40,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your Message',
            }
        ))

    
    class Meta:
        model = MailMessage
        fields = '__all__'