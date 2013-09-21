# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from RentSystem.Rent.models import *
from django.template import *
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
	return render_to_response('Rent/index.html', context_instance=RequestContext(request))	
"""def category(request):
	if request.method == 'POST':
		form = CategoryChoiceForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			catchoice = request.POST.getlist('category_name')
			profile=form.save(commit=False)
			profile.save()
			form.save_m2m()
			catchoice=Category.objects.all().values('category_name')
			cat = Activity.objects.all().filter(id=1).values('activity_name')
			template={'form':form}
#			return HttpResponseRedirect('.')
			return HttpResponseRedirect('/adata/')
	else:
		form = CategoryChoiceForm()
	
	return render_to_response('time_schedule/category_choice.html',{'form': form}, context_instance=RequestContext(request))
def slct(request):
	return render_to_response('time_schedule/slct.html', context_instance=RequestContext(request))
def fdata(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			p=form.save()
			return HttpResponseRedirect('/category/')
			#return HttpResponseRedirect(reverse('project.views.form',args=('1')))
	else:
		form = CategoryForm()
	return render_to_response('time_schedule/form.html', {'form': form}, context_instance=RequestContext(request))
def adata(request):
	if request.method == 'POST':
		form = ActivityForm(request.POST)
		if form.is_valid():
			p=form.save()
			return HttpResponseRedirect('/activity/')
			#return HttpResponseRedirect(reverse('projecjjt.views.form',args=('1')))
	else:
		form = ActivityForm()
	return render_to_response('time_schedule/form1.html', {'form': form}, context_instance=RequestContext(request))
def time(request):
	if request.method == 'POST':
		form = TimeForm(request.POST)
		if form.is_valid():
			p=form.save()
			catchoice = request.POST.getlist('category_name')
			profile=form.save(commit=False)
			profile.save()
			form.save_m2m()
			catchoice=Category.objects.all().values('category_name')
			return HttpResponseRedirect('.')
			
	else:
		form = TimeForm()
	return render_to_response('time_schedule/form2.html', {'form': form}, context_instance=RequestContext(request))
def activity(request):
	
	if request.method == 'POST':
		form = ActivityChoiceForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			catchoice = request.POST.getlist('activity_name')
			profile=form.save(commit=False)
			profile.save()
			form.save_m2m()
			catchoice=Activity.objects.all().values('activity_name')
			template={'form':form}
#			return HttpResponseRedirect('.')
			return HttpResponseRedirect('/time/')
	else:
		form = ActivityChoiceForm()
	
	return render_to_response('time_schedule/activity_choice.html',{'form': form}, context_instance=RequestContext(request))

def main(request):
	return render_to_response('time_schedule/main.html',context_instance=RequestContext(request))

"""
