from django.contrib import admin

from applications.checker.models import Check


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    ...
