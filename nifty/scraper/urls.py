# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.nifty_data, name='nifty_data'),
]
