from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG, STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

if DEBUG:
    urlpatterns += static(STATIC_ROOT, documant_url=STATIC_URL)
