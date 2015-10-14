from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from quotes import views

urlpatterns = [
    url(r'^$', views.QuoteList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.QuoteDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)