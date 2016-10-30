from django.conf.urls import include, url
from .views import order_invoice
from django.conf.urls import url
from .views import render_template, render_donation_template, order_invoice, thank_you

donations = [
    url(r'^$', render_donation_template, name='home'),
    url(r'^orderinvoice/$', order_invoice, name='order_invoice'),
    url(r'^thank-you/$', thank_you, name='thank_you'),
]

urlpatterns = [
    url(r'^$', render_template, name='home'),
    url(r'^donation/', include(donations, namespace='donation')),
]