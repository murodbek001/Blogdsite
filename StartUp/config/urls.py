from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('admin-star/', include('admin_star.urls')),
    path('',include('main.urls'))  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

