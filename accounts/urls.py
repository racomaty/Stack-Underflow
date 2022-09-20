from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)