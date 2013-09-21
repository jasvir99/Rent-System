# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from RentSystem.Rent.models import *
from django.template import *
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(request):
	if request.user.is_active == 1:
		return render_to_response('Rent/index.html', context_instance=RequestContext(request))
			
	else:
		return render_to_response('Rent/index1.html', context_instance=RequestContext(request))

def checkIn(request):
	if request.method == 'POST':
		form = RenterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			room_id = cd['room_id']
			name = cd['name']
			address = cd['address']
			phone_no = cd['phone_no']
			start_date = cd['start_date']
			pro = Renter(room_id = room_id,name = name, address = address, phone_no = phone_no,
			start_date = start_date)
			pro.save()
			return render_to_response('Rent/checkin_ok.html', context_instance=RequestContext(request))
	else:
		form = RenterForm()
		form = {'form':form}
		return render_to_response('Rent/checkin.html', dict(form.items() 
		),context_instance=RequestContext(request))
	
def search(request):
	query = request.GET.get('q', '')
	addquery=request.GET.get('add', '')
	if query:
		qset = (
			Q(name__icontains=query)			
	   	)	
		aset = (
	     	Q(address__icontains=addquery)
		)
		results = Renter.objects.filter(aset).filter(qset).\
		distinct()
	else:
		results = []
	temp = {'results': results,'query': query,}
	return render_to_response("Rent/search.html", dict(temp.items() 
	),context_instance=RequestContext(request))
		
