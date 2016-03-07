from django.shortcuts import render
from .models import UrlAdminModel as Model


def home(request):
    urls = Model.objects.order_by('timeshift').values()
    list_urls = [entry for entry in urls]
    context = {
        'urls': list_urls,
    }
    return render(request, "url_parser/home.html", context)
