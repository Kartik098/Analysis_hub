"""dj_pd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/

"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/' ,logout_view, name='logout'),
    path('register/' ,register_view, name='register'),
    path('performance/', include('products.urls', namespace='products')),
    path('upload/', include('csvs.urls', namespace='csvs')),
    path('customers/', include('customers.urls', namespace='customers'))

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)