from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^p/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # ex: /repository/5/
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    # ex: /repository/5/results/
    url(r'^(?P<id>\d+)/results/$', views.results, name='results'),

]
