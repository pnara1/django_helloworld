#specify patterns to route differernt URLs to their appropriate views

from django.urls import path
from hello import views #from hello directory, import view.py

urlpatterns = [path("", views.home, name='home'),
               ]

