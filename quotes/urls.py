from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<quote_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<quote_id>[0-9]+)/author/$', views.quote_author, name='quote_author'),
    url(r'^(?P<quote_id>[0-9]+)/edit/$', views.edit_quote, name='edit_quote'),
]