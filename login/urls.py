from django.conf.urls import include, url
from . import views
 
urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
]