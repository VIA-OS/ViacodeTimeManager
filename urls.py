from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ViacodeTimeManager.Tasks.views.list_all_tasks'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns()