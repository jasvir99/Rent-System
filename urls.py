from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
#    (r'^accounts/', include('registration.urls')),
#    (r'^$', TemplateView,
#            { 'template': 'index.html' }, 'index'),
    # Examples:
    (r'^$', 'RentSystem.Rent.views.index'),
   # (r'^time_schedule/', include('Timelog.time_schedule.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    

)

