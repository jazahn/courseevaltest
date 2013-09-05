from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from courseeval.admin import admin_site

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^admin/$', 'courseeval.core.index', name='coreIndex'),
    # url(r'^$', 'courseeval.views.home', name='home'),
    # url(r'^courseeval/', include('courseeval.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
