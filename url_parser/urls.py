from django.conf.urls import url
from . import views
from . import parser

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ajax/parse/$', parser.parse),
    url(r'^ajax/refresh/$', parser.refresh),
]
