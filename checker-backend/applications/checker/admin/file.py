from django.contrib import admin

from applications.checker.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
