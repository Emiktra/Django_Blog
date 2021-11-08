from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include("BLOG.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +staticfiles_urlpatterns()
