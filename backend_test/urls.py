from django.conf.urls import include, url
from django.contrib import admin
from url_parser import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'backend_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(urls)),
]
