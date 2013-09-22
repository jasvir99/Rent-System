# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from RentSystem.Rent.models import *
from django.template import *
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Max ,Q, Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.db.models import F
from django import template
from tagging.models import Tag, TaggedItem
from django.core.mail import send_mail        

def index(request):
	if request.user.is_active == 1:
		return render_to_response('Rent/index.html', context_instance=RequestContext(request))
			
	else:
		return render_to_response('Rent/index1.html', context_instance=RequestContext(request))

def checkIn(request):
	if request.method == 'POST':
		if request.user.is_active == 1:
			form = RenterForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				Id = cd['room_id']
				name = cd['name']
				address = cd['address']
				phone_no = cd['phone_no']
				start_date = cd['start_date']
				Room.objects.filter(Id = Id).update(on_rent=1)
				checkin = RenterDetails(room_id = Id, name = name, address = address, phone_no = phone_no,
				start_date = start_date)
				checkin.save()
				return render_to_response('Rent/checkin_ok.html', context_instance=RequestContext(request))
		else:
			return render_to_response('Rent/index1.html', context_instance=RequestContext(request))
	else:
		form = RenterForm()
		room = Room.objects.all()
		form = {'form':form, 'room':room}
		return render_to_response('Rent/checkin.html', dict(form.items() 
		),context_instance=RequestContext(request))
	
def search(request):
	if request.user.is_active == 1:
		query = request.GET.get('q', '')
		addquery=request.GET.get('add', '')
		if query:
			qset = (
				Q(name__icontains=query)			
		   	)	
			aset = (
		     	Q(address__icontains=addquery)
			)
			results = RenterDetails.objects.filter(aset).filter(qset).\
			distinct()
		else:
			results = []
		temp = {'results': results,'query': query,}
		return render_to_response("Rent/search.html", dict(temp.items() 
		),context_instance=RequestContext(request))
	else:
		return render_to_response('Rent/index1.html', context_instance=RequestContext(request))
		
def profile(request):
	if request.user.is_active == 1:
		renter = RenterDetails.objects.filter(id=request.GET['id'])
		temp = {'renter' : renter,}
		return render_to_response('Rent/details.html',dict(temp.\
		items()), context_instance=RequestContext(request))
	else:
		return render_to_response('Rent/index1.html', context_instance=RequestContext(request))

def available(request):
	if request.user.is_active == 1:
		rooms = Room.objects.filter(on_rent=0, Type=1)
		shop = Room.objects.filter(on_rent=0, Type=2)
		temp = {'rooms': rooms,'shop': shop}
		return render_to_response('Rent/available.html',dict(temp.\
		items()), context_instance=RequestContext(request))
	else:
		return render_to_response('Rent/index1.html', context_instance=RequestContext(request))

def payment(request):
	if request.method == 'POST':
		if request.user.is_active == 1:
			form = paymentForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				Id = cd['renter_id']
				electricity = cd['electricity']
				ammount_paid = cd['ammount_paid']
				balance = cd['balance']
				date_of_payment = cd['date_of_payment']
				pay = Accounts(renter_id = Id, electricity = electricity, ammount_paid = ammount_paid, balance = balance,
				date_of_payment = date_of_payment)
				pay.save()
				return render_to_response('Rent/payment_ok.html', context_instance=RequestContext(request))
		else:
			return render_to_response('Rent/index1.html', context_instance=RequestContext(request))
	else:
		form = paymentForm()
		form = {'form':form}
		return render_to_response('Rent/payment.html', dict(form.items() 
		),context_instance=RequestContext(request))
