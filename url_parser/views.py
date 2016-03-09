from django.shortcuts import render
from .models import UrlAdminModel as Model


def home(request):
    urls = Model.objects.order_by('timeshift').values()
    context = {
        'urls': urls,
    }
    return render(request, "url_parser/home.html", context)
