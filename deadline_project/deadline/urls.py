from django.urls import path

from . import views
urlpatterns = [
    path('', views.landing, name='landing'),
    path('<pk>/home', views.home, name='home'),
    path('registration', views.register, name='register'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logoutView, name='logout')

]
