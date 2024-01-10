# expense/urls.py
from django.urls import path
from .views import expense_list, webhook

urlpatterns = [
    path("list/", expense_list, name="expense_list"),
    path("webhook/", webhook, name="webhook"),
]
