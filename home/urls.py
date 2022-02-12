from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('<slug:lang>', home, name='home'),
]

