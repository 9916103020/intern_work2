import os

from django.contrib import admin
from django.urls import path, include

from mysite.core import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import *
from mysite.settings import BASE_DIR

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('image_upload', views.hotel_image_view, name = 'image_upload'),
    # path('success', views.success, name = 'success'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
