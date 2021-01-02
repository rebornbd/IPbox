from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from bladeapp.models import Blade
from .models import Slot


def slotList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  slots = Slot.objects.all()

  p = Paginator(slots, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'slotapp/slots.html', context)


def slotCreate(request):
  if (request.POST):
    name    = request.POST['slotname']
    ip      = request.POST['slotip']
    bladeip = request.POST['blade']
        
    blade = Blade.objects.get(pk=bladeip)
    slot  = Slot(name=name, ip=ip, blade=blade)
    slot.save()
        
    return redirect("/slots")
    
  context = {
    'blades': Blade.objects.all()
  }
  return render(request, 'slotapp/slot_create.html', context=context)


def slotUpdate(request, id):
  slot = Slot.objects.get(pk=id)
    
  if (request.POST):
    name    = request.POST['slotname']
    ip      = request.POST['slotip']
    bladeid = request.POST['blade']

    blade   = Blade.objects.get(pk=bladeid)
    
    slot.name = name
    slot.ip = ip
    slot.blade = blade
    slot.save()
    return redirect("/slots")
    
  context = {
    'slot': slot,
    'blades': Blade.objects.all()
  }
  return render(request, 'slotapp/slot_update.html', context=context)


def slotQuery(request, id):
  slot = Slot.objects.get(pk=id)

  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  vms = slot.vmslots.all()

  p = Paginator(vms, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'vmapp/vms.html', context)
