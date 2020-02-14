from django import forms
from home_page.models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}), required=True, max_length=100)
    emailId = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Your Email'}), required=True, max_length=100)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}), required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}), required=True)

    class Meta:
        model = ContactForm
        fields = ['name', 'emailId', 'subject', 'message', ]

