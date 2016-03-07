from django.contrib import admin
from .models import UrlAdminModel
from .forms import UrlForm


@admin.register(UrlAdminModel)
class UrlAdmin(admin.ModelAdmin):
    list_display = ["url", "timeshift", "success"]
    readonly_fields = ('time', 'title', 'h1', 'charset')
    form = UrlForm
