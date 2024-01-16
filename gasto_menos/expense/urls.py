# expense/urls.py
from django.urls import path
from .views import list, webhook

urlpatterns = [
    path("webhook/", webhook, name="webhook"),
    path("list/", list, name="list"),
]
