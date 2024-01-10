# expense/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods

from .models import Expense
from .utils import process_text
from user.models import UserProfile
from category.models import Category


import json
import datetime


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, "expense_list.html", {"expenses": expenses})


@csrf_exempt  # This decorator is used to exempt the view from CSRF protection (for webhook endpoints)
@require_POST  # This decorator ensures that only POST requests are allowed
@require_http_methods(["POST"])
def webhook(request):
    try:
        data = json.loads(request.body.decode("utf-8"))

        phone = data["from"]
        message = data["body"]

        expense = process_text(message)

        user, _ = UserProfile.objects.get_or_create(phone=phone)
        category = Category.objects.get(name=expense["category"])

        Expense.objects.create(
            user=user,
            message=message,
            amount=expense["amount"],
            category=category,
            currency=expense["currency"],
            date=datetime.datetime.now(),
        )

        res = f"Created expense in {expense['category']} for {expense['amount']} {expense['currency']}"

        response_data = {
            "success": True,
            "response": res,
        }
        return JsonResponse(response_data)
    except Exception as e:
        response_data = {
            "success": False,
            "error": str(e),
        }
        return JsonResponse(response_data, status=500)
