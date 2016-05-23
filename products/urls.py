from django.conf.urls import include, url

from .views import product_detail_view, ProductListView, CountryListView

urlpatterns = [
    # Country
    url(r'^country/$', CountryListView.as_view(), name='country_list'),

    # Product
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<id>\d+)/$', product_detail_view, name='product_detail'),
    # url(r'^country/(?P<countryId>\d+)/$', ProductListView.as_view(), name='product_list'),
]
