from django.urls import path
from .views import about

urlpatterns = [
    path('', about, name='about'),
    path('<slug:lang>', about, name='about'),
]

