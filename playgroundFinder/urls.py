from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'playgroundFinder.views.home', name='home'),
    # url(r'^playgroundFinder/', include('playgroundFinder.foo.urls')),
    url(r'^hello-world/$', 'playgroundApp.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
