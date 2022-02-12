from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('categories/', include('categories.urls'), name='categories'),
    path('about_product/', include('about_product.urls'), name='about_product'),
    path('contacts/', include('contacts.urls'), name='contacts'),
    path('about/', include('about.urls'), name='about'),
    path('reviews/', include('reviews.urls'), name='reviews'),
    path('site/admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

