from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse

from accounts.views import generalUser, adminUser
from siteapp.models import Site
from .models import Rack


def rackList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  racks = Rack.objects.all()

  p = Paginator(racks, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
    'generalUser': generalUser(request.user),
    'adminUser': adminUser(request.user)
  }
  return render(request, 'rackapp/racks.html', context=context)


@login_required(login_url='accountsapp:login')
def rackCreate(request):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))
  
  if (request.POST):
    name    = request.POST['rackname']
    ip      = request.POST['rackip']
    siteid  = request.POST['site']
        
    site    = Site.objects.get(pk=siteid)

    rack    = Rack(name=name, ip=ip, site=site)
    rack.save()
    return redirect("/racks")

  context = {
    'sites': Site.objects.all()
  }
  return render(request, 'rackapp/rack_create.html', context=context)


@login_required(login_url='accountsapp:login')
def rackUpdate(request, id):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))

  rack = Rack.objects.get(pk=id)
  if (request.POST):
    name    = request.POST['rackname']
    ip      = request.POST['rackip']
    # siteid  = request.POST['site']
    # site = Site.objects.get(pk=siteid)
        
    rack.name = name
    rack.ip = ip
    # rack.site = site
    rack.save()
    return redirect("/racks")
    
  context = {
    'rack': rack,
    'sites': Site.objects.all()
  }
  return render(request, 'rackapp/rack_update.html', context=context)


@login_required(login_url='accountsapp:login')
def rackQuery(request, id):
  rack = Rack.objects.get(pk=id)

  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  blades = rack.blades.all()

  p = Paginator(blades, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'bladeapp/blades.html', context)

