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
  pass

def bladeUpdate(request, id):
  pass

