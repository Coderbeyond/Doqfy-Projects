from django.shortcuts import render, redirect, get_object_or_404
from .models import TextSnippet
from .forms import SecretKeyForm, TextSnippetForm
from django.urls import reverse



def create_snippet(request):
    if request.method == 'POST':
        form = TextSnippetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            secret_key = form.cleaned_data['secret_key'] 
            snippet = TextSnippet.objects.create(content=content, secret_key=secret_key)
            
            shareable_url = request.build_absolute_uri(reverse('view_snippet', args=[str(snippet.id)]))
            
            return render(request, 'pastelock/shareurl.html', {'shareable_url': shareable_url})
    else:
        form = TextSnippetForm()
    return render(request, 'pastelock/createsnippet.html', {'form': form})


def view_snippet(request, snippet_id):
    snippet = get_object_or_404(TextSnippet, id=snippet_id)
    key_form = SecretKeyForm(request.GET or None)
    decrypted_content = None

    if key_form.is_valid():
        entered_key = key_form.cleaned_data['key']
        if entered_key == snippet.secret_key:
            decrypted_content = snippet.content
        else:
            key_form.add_error('key', 'Invalid secret key.')

    return render(request, 'pastelock/viewsnippet.html', {
        'snippet': snippet,
        'key_form': key_form,
        'decrypted_content': decrypted_content
    })

