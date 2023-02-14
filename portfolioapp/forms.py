from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=50)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=2000)