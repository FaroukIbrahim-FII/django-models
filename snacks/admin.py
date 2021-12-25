from django.contrib import admin
from .models import Snack


# admin.site.register(Snack)

@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ['name', 'purchaser', 'description']
    search_fields = ['purchaser']