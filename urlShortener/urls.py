# Aysin Oruz

from django.conf.urls import patterns, include, url
from django.contrib import admin
from projects.views import ShortUrlRedirectView

urlpatterns = patterns('',

    url(r'^$', 'projects.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<short_url>[a-z0-9]+)/?$', ShortUrlRedirectView.as_view(), name='redirect',),
)
