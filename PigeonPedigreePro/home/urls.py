from django.urls import path
from .views import *

urlpatterns=[
    path('', Home, name='Home'),
    path('About', About, name='About'),
    path('Price', Price, name='Price'),
    path('Demo', Demo, name='Demo'),
    path('Contact', Contact, name='Contact'),
    path('Pedigree', Pedigree, name='Pedigree'),
    path('Login', Login, name='Login'),
    path('Logout', Logout, name='Logout'),
    path('Registration', Registration, name='Registration'),
    path('privacy_policy', privacy_policy, name='privacy_policy'),
]