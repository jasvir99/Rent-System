from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from RentSystem.Rent.models import *
urlpatterns = patterns('RentSystem.Rent.views',
		(r'^$', 'index'),
		(r'^checkin', 'checkIn'),

		(r'^viewprofile', 'search'),
""" 
		(r'^collect_ammount_find', 'collectAmmountFind'),
		(r'^collect_ammount', 'collectAmmount'),
		(r'^collect_ammount_ok', 'collectAmmountOk'),
		(r'^ammount_not_recieved', 'ammountNotRecieved'),

"""
)
