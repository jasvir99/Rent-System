from django.contrib import admin
from RentSystem.Rent.models import *

"""
class Cat_nameAdmin(admin.ModelAdmin):
	list_display = ('category_name',)
	search_fields = ('category_name',)
	list_filter = ['category_name']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('cat_id',)
	search_fields = ('cat_id',)
	
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('act_name',)
	search_fields = ('act_name',)
	list_filter = ['act_name']

class TimeAdmin(admin.ModelAdmin):
	list_display = ('time_name',)
	search_fields = ('time_name',)
	list_filter = ['time_name']

admin.site.register(Cat_name,Cat_nameAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Time,TimeAdmin)
"""
