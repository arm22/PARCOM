from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.study_list, name='study_list'),
    url(r'^study/(?P<pk>\d+)/$', views.study_detail, name='study_detail'),
    url(r'^study/new/$', views.study_new, name='study_new'),
    url(r'^study/(?P<pk>\d+)/edit/$', views.study_edit, name='study_edit'),
    url(r'^study/(?P<pk>\d+)/comment/$', views.add_comment_to_study, name='add_comment_to_study'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^settings/$', views.user_profile, name='settings'),
]