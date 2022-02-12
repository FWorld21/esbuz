from django.urls import path
from .views import categories, products

urlpatterns = [
    path('', categories, name='categories'),
    path('<slug:lang>', categories, name='categories'),
    path('<slug:slug>/', products, name='products'),
    path('<slug:slug>/<slug:lang>/', products, name='products'),
]

