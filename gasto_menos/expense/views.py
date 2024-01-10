# expense/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods

from models import Expense
from utils import process_text

import json


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, "expense_list.html", {"expenses": expenses})


@csrf_exempt  # This decorator is used to exempt the view from CSRF protection (for webhook endpoints)
@require_POST  # This decorator ensures that only POST requests are allowed
@require_http_methods(["POST"])
def webhook(request):
    try:
        data = request.POST.get("data")  # Assuming you are sending data as form data
        data = json.loads(
            data
        )  # If data is sent as JSON, you may need to parse it accordingly

        message_from = data["data"]["from"]
        message_msg = data["data"]["body"]

        expense = process_text(message_msg)

        response_data = {
            "success": True,
            "data": expense,
        }
        return JsonResponse(response_data)
    except Exception as e:
        response_data = {
            "success": False,
            "error": str(e),
        }
        return JsonResponse(response_data, status=500)
