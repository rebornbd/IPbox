from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from siteapp.models import Site
from rackapp.models import Rack
from .models import Blade


def bladeList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  blades = Blade.objects.all()

  p = Paginator(blades, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'bladeapp/blades.html', context)


def bladeCreate(request):
  if (request.POST):
    name    = request.POST['bladename']
    ip      = request.POST['bladeip']
    rackid  = request.POST['rack']
        
    rack    = Rack.objects.get(pk=rackid)

    blade   = Blade(name=name, ip=ip, rack=rack)
    blade.save()
    return redirect("/blades")

  context = {
    'racks': Rack.objects.all()
  }
  return render(request, 'bladeapp/blade_create.html', context=context)


def bladeUpdate(request, id):
  blade = Blade.objects.get(pk=id)
    
  if (request.POST):
    name    = request.POST['bladename']
    ip      = request.POST['bladeip']
    rackid  = request.POST['rack']

    rack = Rack.objects.get(pk=rackid)
    
    blade.name = name
    blade.ip = ip
    blade.rack = rack
    blade.save()
    return redirect("/blades")
    
  context = {
    'blade': blade,
    'racks': Rack.objects.all()
  }
  return render(request, 'bladeapp/blade_update.html', context=context)


def bladeQuery(request, id):
  blade = Blade.objects.get(pk=id)

  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  slots = blade.slots.all()

  p = Paginator(slots, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'slotapp/slots.html', context)
