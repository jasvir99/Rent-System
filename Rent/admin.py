from django.contrib import admin
from RentSystem.Rent.models import *

class RoomAdmin(admin.ModelAdmin):
	list_display = ('Id','rent','Type',)
	search_fileds = ('Id',)
	list_filter = ['Type']
	exclude = ['Id']

admin.site.register(Room,RoomAdmin)
