from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^addtrip2$', views.addtrip2),
    url(r'^destination/(?P<trip_id>\d+)$', views.destination),
    url(r'^join/(?P<trip_id>\d+)$', views.join),
    url(r'^profile/(?P<user_id>\d+)$', views.profile),
    # url(r'^delete/(?P<trip_id>\d+)$', views.delete),
]
