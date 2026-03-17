__all__ = []

from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    list_filter = ['date_joined']
    search_fields = ['email', 'first_name', 'last_name']
