
from django.conf.urls import url

from . import views, account, request, itinerary

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # account
    url(r'^account/login', views.login, name='login'),
    url(r'^account/logout', views.logout, name='logout'),
    url(r'^account/auth', views.authenticate, name='authenticate'),
    url(r'^account/reg', views.register, name='register'),
    url(r'^account/profile', account.profile, name='profile'),

    # request
    url(r'^request/load', request.load_request, name='load_request'),
    url(r'^request/create', request.create_request, name='create_request'),
    url(r'^request/detail/(?P<request_id>[0-9]+)', request.confirm_request, name='confirm_request'),
    url(r'^request/cancel/(?P<request_id>[0-9]+)', request.cancel, name='cancel'),
    url(r'^request/assign/(?P<request_id>[0-9]+)', request.assign_request, name='assign_request'),
    # search
    url(r'^search', views.search, name='search'),

    # itinerary
    url(r'^itinerary/load', itinerary.load_itinerary, name='load_itinerary'),
    url(r'^itinerary/create', itinerary.create_itinerary, name='create_itinerary'),

]
