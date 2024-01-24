"""
URL configuration for crp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
from agencies.views import (
    agencies_create_view,
    agencies_detail_view,
    agencies_search_view,
)
from .views import home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("agencies/", agencies_search_view, name="agencies"),
    path("agencies/create/", agencies_create_view, name="agencies-create"),
    path("agencies/<int:id>/", agencies_detail_view, name="agencies-detail"),
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
