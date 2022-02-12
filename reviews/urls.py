from django.urls import path
from .views import *

urlpatterns = [
    path('', reviews, name='reviews'),
    path('<slug:lang>', reviews, name='reviews'),
]

