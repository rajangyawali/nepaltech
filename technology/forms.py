from django import forms
from . import models


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class SubscriberForm(forms.Form):
    subscriber = forms.EmailField(required=True)