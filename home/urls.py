
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # account
    url(r'^account/login', views.login, name='login'),
    url(r'^account/logout', views.logout, name='logout'),
    url(r'^account/auth', views.authenticate, name='authenticate'),
    url(r'^account/reg', views.register, name='register'),
    # request
    url(r'^request/load', views.load_request, name='load_request'),
    url(r'^request/create', views.create_request, name='create_request'),

]
