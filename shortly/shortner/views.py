from django.shortcuts import render, redirect
from .models import ShortenedURL
from .forms import URLShortenForm

def shorten_url(request):
    if request.method == 'POST':
        form = URLShortenForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = ShortenedURL.objects.create(original_url=original_url)
            return render(request, 'shortner/shortned_url.html', {'short_url': short_url, 'request': request})
    else:
        form = URLShortenForm()
    return render(request, 'shortner/url_form.html', {'form': form})

def redirect_to_original(request, short_code):
    short_url = ShortenedURL.objects.get(short_code=short_code)
    return redirect(short_url.original_url)
