from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UserLoginForm, RegistrationForm, EmailForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
import logging
logging.basicConfig(level=logging.INFO) # Here
logging.debug("Log message goes here.")
logging.info("Log message goes here.")
logging.warning("Log message goes here.")
logging.error("Log message goes here.")
logging.critical("Log message goes here.")
# Create your views here.
welcome = "Welcome to DEADLINE"
sitetitle = "DEADLINE"
description = "Prioritize work loads and activities"
landingNavs = {'About': 'about', 'Contact': 'contact','Login':'landing', 'Register': 'register'}
def landing(request):
    if request.method =='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect(home, username=user.username)

    else:
        form = UserLoginForm()
    context = {
     'welcome':welcome, 'description':description, 'form':form, 'navlist':landingNavs, 'sitetitle' :sitetitle,
    }
    return render(request, 'deadline/landing.html', context)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/username/')
    else:
        form = RegistrationForm()

    context = {
        'form':form, 'navlist':landingNavs, 'sitetitle':sitetitle,
    }
    return render(request, "deadline/register.html", context)

def about(request):
    linkedin="https://www.linkedin.com/in/jerusalem-moore/"
    school="California State University, Chico - Chico, CA	December 2021"
    degree="Bachelor of Science in Computer Science"
    github="https://github.com/jerusalemmoore"
    author = "Jerusalem Moore"
    mission = """This is a personal project I am developing in order to build
    on my web programming experience as well as get stronger with
    both Python and the Django framework which is written in Python."""
    goal =  """I hope this Application can function as a task organizer that
    provides transparency on what needs to be
    done and when in a way that allows you to allot time properly to individual tasks"""
    contact ="""I am always interested in learning something new or improving on my work.
    If you have any comments, constructive criticism or tips/pointers. I would love
    to hear from you. Just leave a comment on my contact page.
    """
    context = {
        'sitetitle':sitetitle, 'navlist':landingNavs, 'author':author,
        'mission':mission,'goal':goal, 'contact':contact, 'linkedin':linkedin,
        'github':github, 'school':school, 'degree':degree
    }
    return render(request, "deadline/about.html", context)

def contact(request):
    if request.method =='POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                None,
                [settings.DEFAULT_RECIPIENT],
            )
    else:
        form = EmailForm()
    context = {
        'sitetitle':sitetitle, 'navlist':landingNavs, 'form':form
    }
    return render(request, "deadline/contact.html", context)

def home(request, username):
    navlist = {'Logout': 'logout'}
    buttonLabels = ['Create Course', 'Create Appointment', "My Courses"]
    context = {'navlist':navlist, 'sitetitle':sitetitle, 'buttonLabels':buttonLabels}
    return render(request, "deadline/home.html", context)
    # return render(request, "deadline/home.html", context)
def logoutView(request):
    logout(request)
    return redirect(landing)
