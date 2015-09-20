from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update$', views.update_quote, name='update_quote'),
    url(r'^new/$', views.new_quote, name="new_quote"),
    url(r'^create/$', views.create_quote, name="create_quote"),
]