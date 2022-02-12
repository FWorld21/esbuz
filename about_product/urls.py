from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/<slug:product_slug>/', about_product, name='about_product'),
    path('<slug:slug>/<slug:product_slug>/<slug:lang>/', about_product, name='about_product'),
    path('<slug:product_slug>/', about_product, name='about_product'),
    path('<slug:product_slug>/<slug:lang>/', about_product, name='about_product'),
]
