from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('user/', include('user.urls')),
    path('basicview/', include('article.urls')),
]
