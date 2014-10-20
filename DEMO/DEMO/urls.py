from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^APP/$', 'APP.views.Index', name='Index'),
    url(r'^MAIN/$', 'APP.views.MenuMain', name='MenuMain'),
    url(r'^MNT/APO/$', 'APP.views.MntApoderado', name='MntApoderado'),
    url(r'^admin/', include(admin.site.urls)),
    # Static
	(r'css/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + '/static/css'}),
	(r'img/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.STATIC_ROOT + '/static/img'}),
	(r'js/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + '/static/js'}),
	(r'fonts/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + '/static/fonts'}),
)