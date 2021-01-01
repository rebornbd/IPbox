from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Site


def siteList(request):
  dataPerPage = 5
  sites = Site.objects.all()

  pageNum = request.GET.get('page', 1)
  
  p = Paginator(sites, dataPerPage)
  page_obj = p.page(pageNum)

  context = {
    'page_obj': page_obj
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


def home(request):
  return render(request, 'siteapp/sites.html')