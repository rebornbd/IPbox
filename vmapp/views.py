from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse

from accounts.views import generalUser, adminUser
from clusterapp.models import Cluster
from slotapp.models import Slot
from .models import VM


def vmList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  vms = VM.objects.all()

  p = Paginator(vms, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
    'generalUser': generalUser(request.user),
    'adminUser': adminUser(request.user)
  }
  return render(request, 'vmapp/vms.html', context)


@login_required(login_url='accountsapp:login')
def vmCreate(request):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))
  
  if (request.POST):
    name      = request.POST['vmname']
    hostname  = request.POST['vmhostname']
    ip        = request.POST['vmip']
        
    slotid    = request.POST['slot']
    clusterid = request.POST['cluster']
        
    slot    = Slot.objects.get(pk=slotid)
    cluster = None
    if (clusterid != ""):
      cluster = Cluster.objects.get(pk=clusterid)
            
    vm = VM(name=name, hostname=hostname, ip=ip, slot=slot, cluster=cluster)
    vm.save()
        
    return redirect("/vms")
    
  context = {
    'slots': Slot.objects.all(),
    'clusters': Cluster.objects.all(),
  }
  return render(request, 'vmapp/vm_create.html', context=context)


@login_required(login_url='accountsapp:login')
def vmUpdate(request, id):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))
  
  vm = VM.objects.get(pk=id)
  if (request.POST):
    name        = request.POST['vmname']
    hostname    = request.POST['vmhostname']
    ip          = request.POST['vmip']
        
    slotid      = request.POST['slot']
    clusterid   = request.POST['cluster']
        
    slot    = Slot.objects.get(pk=slotid)
    cluster = None
    if (clusterid != ""):
      cluster = Cluster.objects.get(pk=clusterid)

    vm.name = name
    vm.hostname = hostname
    vm.ip = ip
    vm.slot = slot
    vm.cluster = cluster
    vm.save()
    return redirect("/vms")
    
  context = {
    'vm': vm,
    'slots': Slot.objects.all(),
    'clusters': Cluster.objects.all(),
  }
  return render(request, 'vmapp/vm_update.html', context=context)


def vmQuery(request, id):
  pass
