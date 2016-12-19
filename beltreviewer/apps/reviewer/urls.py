from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^add_review$', views.add_review),
    url(r'^$user_review', views.user_review),
    url(r'^$review', views.review),

]
