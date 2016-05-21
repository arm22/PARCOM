from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.study_list, name='study_list'),
    url(r'^study/(?P<pk>\d+)/$', views.study_detail, name='study_detail'),
]