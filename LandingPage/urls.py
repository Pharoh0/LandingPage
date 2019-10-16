from django.http import Http404
from django.urls import path
from . import views

app_name = "LandingPage"

urlpatterns = [
    path('', views.form_page, name='form_page'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('thankyounot/', views.thank_you_not, name='thank_you_not'),

]
#path('', views.user, name='user'),
