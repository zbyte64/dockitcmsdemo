from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cmsdemo.views.home', name='home'),
    # url(r'^cmsdemo/', include('cmsdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('', (r'', include('django.contrib.staticfiles.urls')))

    urlpatterns += patterns('django.views',
        (r'^media/(?P<path>.*)$', 'static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

