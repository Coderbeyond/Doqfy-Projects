from django.urls import path
from pastelock.views import create_snippet, view_snippet

urlpatterns = [
    path('', create_snippet, name='create_snippet'),  # Landing page (create snippet form)
    path('create/', create_snippet, name='create_snippet'),
    path('<uuid:snippet_id>/', view_snippet, name='view_snippet'),
]
