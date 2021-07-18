from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse

from accounts.views import generalUser, adminUser
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
    'generalUser': generalUser(request.user),
    'adminUser': adminUser(request.user)
  }
  return render(request, 'slotapp/slots.html', context)


@login_required(login_url='accountsapp:login')
def slotCreate(request):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))
  
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


@login_required(login_url='accountsapp:login')
def slotUpdate(request, id):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))
  
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


@login_required(login_url='accountsapp:login')
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
