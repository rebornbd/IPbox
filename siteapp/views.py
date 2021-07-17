from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from rackapp.models import Rack
from .models import Site
from accounts.views import generalUser, adminUser


# @login_required(login_url='accountsapp:login')
def siteList(request):
  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  sites = Site.objects.all()
  
  p = Paginator(sites, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
    'generalUser': generalUser(request.user),
    'adminUser': adminUser(request.user)
  }
  return render(request, 'siteapp/sites.html', context=context)


def siteCreate(request):
  if (request.POST):
    name = request.POST['sitename']

    site = Site(name=name)
    site.save()
    return redirect("/sites")
  return render(request, 'siteapp/site_create.html')


def siteUpdate(request, id):
  site = Site.objects.get(pk=id)

  if (request.POST):
    site.name = request.POST['sitename']
    site.save()
    return redirect('/sites')
    
  context = {
    'site': site
  }
  return render(request, 'siteapp/site_update.html', context)


def siteQuery(request, id):
  site = Site.objects.get(pk=id)

  dataPerPage = 5
  pageNum = request.GET.get('page', 1)
  racks = site.racks.all()

  p = Paginator(racks, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj,
  }
  return render(request, 'rackapp/racks.html', context)
