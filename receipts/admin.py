from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt


# Register your models here.
@admin.register(ExpenseCategory, Account, Receipt)
class ReceiptsAdmin(admin.ModelAdmin):
    pass
