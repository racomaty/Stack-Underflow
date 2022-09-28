from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('messages/', include('chat.urls')),
    path("ckeditor/", include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})]


handler404 = 'main.views.not_found'