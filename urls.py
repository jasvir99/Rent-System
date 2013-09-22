from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    (r'^$', 'RentSystem.Rent.views.index'),
	(r'^main/', include('RentSystem.Rent.urls')),
   
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),

)

