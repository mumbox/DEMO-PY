from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'APP.views.Index', name='Index'),
    url(r'^admin/', include(admin.site.urls)),
)