'''
Created on 2015年11月23日

@author: Administrator
'''
from django.conf.urls import url

from fafer import views

urlpatterns = [
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
]

