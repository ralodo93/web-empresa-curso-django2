"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # paths from core
    path("", include("core.urls")),
    # paths from services
    path("services/", include("services.urls")),
    # paths from blog
    path("blog/", include("blog.urls")),
    # paths from pages
    path("page/", include("pages.urls")),
    # paths from contact
    path("contact/", include("contact.urls")),
    # admin
    path("admin/", admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)