from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.study_list, name='study_list'),
    url(r'^study/(?P<pk>\d+)/$', views.study_detail, name='study_detail'),
    url(r'^study/new/$', views.study_new, name='study_new'),
    url(r'^study/(?P<pk>\d+)/edit/$', views.study_edit, name='study_edit'),
]