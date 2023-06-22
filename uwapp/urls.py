from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
#    path('newsite',views.newsite,name='newsite'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('contact/',views.contact,name='contact'),
    path('info/',views.info,name='info'),
    path('export/',views.export)
    ]
