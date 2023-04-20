from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory, Account


class CreateForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]


class CreateCategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]


class CreateAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            "name",
            "number",
        ]
