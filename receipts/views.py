from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import CreateForm


# Create your views here.
@login_required
def receipts_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_list": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            receipts = form.save(commit=False)
            receipts.purchaser = request.user
            receipts.save()
            return redirect("home")
    else:
        form = CreateForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)
