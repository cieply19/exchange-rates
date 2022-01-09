from django.contrib import admin
from .models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["crypto_name", "usd_rate", "pln_rate", "date"]
    list_filter = ["crypto_name"]
    search_fields = ["date"]
    search_help_text = "Data filter YYYY-MM-DD"
