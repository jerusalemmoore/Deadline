from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
welcome = "Welcome to MY SCRAPER"
sitetitle = "MY SCRAPER"
description = "Personalized web scraper that suits your shopping preferences"

def base(request):
    return render(request, 'scraper/base.html', {'sitetitle':sitetitle})
def landing(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/username/')
    else:
        form = LoginForm()
    navlist = ['About','Contact','Register']
    context = {
     'welcome':welcome, 'description':description, 'form':form, 'navlist':navlist, 'sitetitle' :sitetitle
    }
    return render(request, 'scraper/landing.html', context)
def registration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/username/')
    else:
        form = RegistrationFrom()
    navlist = ['About', 'Contact', 'Register']
    context {
        'form':form, 'navlist':navlist, 'sitetitle':sitetitle
    }
    return render(request, "scraper/regregistration.html", context)
