from django.db import models
from django.forms import ModelForm,TextInput,ModelChoiceField
from django import forms
import datetime
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from tagging.fields import TagField
from tagging.models import Tag
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
#class UserRegister(models.Model):
#	Name=models.CharField(max_length=100)

class Room(models.Model):
	Type = models.IntegerField(max_length=2)
	rent = models.IntegerField(max_length=100)
	on_rent = models.IntegerField(max_length=2)
	def __unicode__(self):
		return self.Id

class Renter(models.Model):
	room_id = models.ForeignKey(Room)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	phone_no = models.CharField(max_length=50)
	photo = models.CharField(max_length=50)
	start_date = models.DateField()
	def __unicode__(self):
		return self.name

class Accounts(models.Model):
	renter_id = models.ForeignKey(Renter)
	ammount_paid = models.IntegerField(max_length=100)
	balance = models.IntegerField(max_length=100)
	date_of_payment = models.DateField()
	def __unicode__(self):
		return self.renter_id

class Fixed_Charges(models.Model):
	title = models.CharField(max_length=100)
	ammount = models.IntegerField(max_length=100)
	def __unicode__(self):
		return self.renter_id
"""class Category(models.Model):
	category_name=models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
        	return self.category_name
"""

