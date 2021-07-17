from django.shortcuts import redirect


def ipboxHomePage(request):
    return redirect('siteapp:sites')
