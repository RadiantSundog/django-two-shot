from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import CreateForm, CreateCategoryForm


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


@login_required
def create_category(request):
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            receipts = form.save(commit=False)
            receipts.owner = request.user
            receipts.save()
            return redirect("category_list")
    else:
        form = CreateCategoryForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create_category.html", context)


@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {"categories": categories}
    return render(request, "receipts/categories.html", context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {"accounts": accounts}
    return render(request, "receipts/accounts.html", context)
