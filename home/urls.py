
from django.conf.urls import url

from . import views, account, request, itinerary

urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^auth', views.authenticate, name='authenticate'),
    url(r'^reg', views.register, name='register'),

    # account
    url(r'^account/landing', account.landing, name='landing'),
    url(r'^account/orders', account.orders, name='orders'),

    # request
    url(r'^request/load', request.load_request, name='load_request'),
    url(r'^request/create', request.create_request, name='create_request'),
    url(r'^request/detail/(?P<request_id>[0-9]+)', request.take_request, name='take_request'),
    url(r'^request/cancel/(?P<request_id>[0-9]+)', request.cancel, name='cancel'),
    url(r'^request/ship/(?P<request_id>[0-9]+)', request.ship, name='ship'),
    url(r'^request/complete/(?P<request_id>[0-9]+)', request.complete, name='complete'),
    url(r'^request/deliver/(?P<request_id>[0-9]+)', request.deliver, name='deliver'),
    url(r'^request/assign/(?P<request_id>[0-9]+)', request.assign_request, name='assign_request'),
    # search
    url(r'^search', views.search, name='search'),

    # itinerary
    url(r'^itinerary/load', itinerary.load_itinerary, name='load_itinerary'),
    url(r'^itinerary/create', itinerary.create_itinerary, name='create_itinerary'),

]
