from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UserLoginForm, RegistrationForm, EmailForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
import logging
logger=logging.getLogger('myLogger')
# Create your views here.
welcome = "Welcome to DEADLINE"
sitetitle = "DEADLINE"
description = "Prioritize work loads and activities"
landingNavs = {'About': 'about', 'Contact': 'contact','Login':'landing', 'Register': 'register'}
def landing(request):
    if request.method =='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user1 = authenticate(request, email=form.cleaned_data['id'], password=form.cleaned_data['password'])
            user2 = authenticate(request, username=form.cleaned_data['id'], password=form.cleaned_data['password'])
            logger.error('user')
            logger.error(user1)
            logger.error(user2)
            if user1 is not None:
                login(request,user1)
                return redirect(home, pk=user1.pk)
            elif user2 is not None:
                login(request, user2)
                return redirect(home,pk=user2.pk)


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
            form.save()
            # logger.error("the password" + form.cleaned_data['password'])
            return redirect(landing)
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
    formDescription = """Please leave send any comments/tips/inquiries through this form. Don't forget to leave contact info
    if you'd like me to get back to you"""
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
        'sitetitle':sitetitle, 'navlist':landingNavs, 'form':form, 'formDescription':formDescription
    }
    return render(request, "deadline/contact.html", context)

def home(request, pk):
    navlist = {'Logout': 'logout'}
    buttonLabels = ['Create Course', 'Create Appointment', "My Courses"]
    context = {'navlist':navlist, 'sitetitle':sitetitle, 'buttonLabels':buttonLabels}
    return render(request, "deadline/home.html", context)
    # return render(request, "deadline/home.html", context)
def logoutView(request):
    logout(request)
    return redirect(landing)
