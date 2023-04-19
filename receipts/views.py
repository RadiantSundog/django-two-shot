from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt


# Create your views here.
def receipt_list(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt_list": receipt,
    }
    return render(request, "receipts/list.html", context)
