from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse

from accounts.views import generalUser, adminUser
from slotapp.models import Slot
from vmapp.models import VM
from .models import Cluster


def clusterList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  clusters = Cluster.objects.all()

  p = Paginator(clusters, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
    'generalUser': generalUser(request.user),
    'adminUser': adminUser(request.user)
  }
  return render(request, 'clusterapp/clusters.html', context)


@login_required(login_url='accountsapp:login')
def clusterCreate(request):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))
  
  if (request.POST):
    name      = request.POST['clustername']
    ip        = request.POST['clusterip']
    lb_ip     = request.POST['clusterlb_ip']
    bootstrap = request.POST['clusterbootstrap']
        
    cluster = Cluster(name=name, ip=ip, lb_ip=lb_ip, bootstrap=bootstrap)
    cluster.save()
    return redirect("/clusters")
  
  return render(request, 'clusterapp/cluster_create.html')


@login_required(login_url='accountsapp:login')
def clusterUpdate(request, id):
  if not adminUser(request.user):
    return HttpResponseRedirect(reverse('homepage'))

  cluster = Cluster.objects.get(pk=id)
  if (request.POST):
    name      = request.POST['clustername']
    ip        = request.POST['clusterip']
    lb_ip     = request.POST['clusterlb_ip']
    bootstrap = request.POST['clusterbootstrap']
        
    cluster.name = name
    cluster.ip = ip
    cluster.lb_ip = lb_ip
    cluster.bootstrap = bootstrap
        
    cluster.save()
    return redirect("/clusters")
    
  context = {
    'cluster': cluster,
  }
  return render(request, 'clusterapp/cluster_update.html', context=context)


def clusterQuery(request, id):
  pass
