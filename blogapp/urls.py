from django.urls import path
from .views import dashboard, register, compose, search_users
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('compose/', compose, name='compose'),
    path('search_users/', search_users, name='search_users'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blogapp/logged_out.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)