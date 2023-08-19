from django import forms

class URLShortenForm(forms.Form):
    original_url = forms.URLField(label="Enter your URL", widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}))
