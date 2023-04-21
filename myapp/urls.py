from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name='home'),
    path('intro',views.intro, name='intro'),
    path('education',views.education, name='education'),
    path('project',views.project, name='project'),
    path('contact',views.contact, name='contact'),
]
