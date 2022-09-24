from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('editProfile', editProfile, name="editProfile"),
]