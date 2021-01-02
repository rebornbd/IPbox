from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from slotapp.models import Slot
from clusterapp.models import Cluster
from .models import VM


def vmList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  vms = VM.objects.all()

  p = Paginator(vms, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'vmapp/vms.html', context)


def vmCreate(request):
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


def vmUpdate(request, id):
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
