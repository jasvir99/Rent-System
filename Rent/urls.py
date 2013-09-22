from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from RentSystem.Rent.models import *
urlpatterns = patterns('RentSystem.Rent.views',
		(r'^$', 'index'),
		(r'^checkin/$', 'checkIn'),
		(r'^viewprofile/$', 'search'),
		(r'^profile/$', 'profile'),
)
