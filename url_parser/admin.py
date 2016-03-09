from django.contrib import admin
from .models import UrlAdminModel
from .forms import UrlForm


@admin.register(UrlAdminModel)
class UrlAdmin(admin.ModelAdmin):
    # fields that can be changed from admin menu
    list_display = ["url", "timeshift", "success"]

    # fields that will be parsed, so they cannot be changed from admin menu
    readonly_fields = ('time', 'title', 'h1', 'charset')
    form = UrlForm
