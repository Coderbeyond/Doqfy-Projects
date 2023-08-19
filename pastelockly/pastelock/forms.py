from django import forms

class TextSnippetForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    secret_key = forms.CharField(max_length=50, required=False, widget=forms.PasswordInput)

class SecretKeyForm(forms.Form):
    key = forms.CharField(label="Secret Key", max_length=100, widget=forms.PasswordInput)
