from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^quotes/', include('quotes.urls', namespace="quotes")),
    url(r'^admin/', include(admin.site.urls)),
]
