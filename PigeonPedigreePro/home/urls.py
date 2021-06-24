from django.urls import path
from .views import *

urlpatterns=[
    path('', Home, name='Home'),
    path('About', About, name='About'),
    path('Price', Price, name='Price'),
    path('Demo', Demo, name='Demo'),
    path('Contact', Contact, name='Contact'),
    path('Pedigree', Pedigree, name='Pedigree'),
]