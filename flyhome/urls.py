from django.conf.urls import patterns, url

from flyhome.views import default

urlpatterns = patterns('',
	url(r'^$', default.as_view(), name='flyhome-default')
)