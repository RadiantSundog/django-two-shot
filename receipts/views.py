from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt


# Create your views here.
def receipts_list(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts_list": receipts,
    }
    return render(request, "receipts/list.html", context)
