"""ChinaBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Quotes import views as quotes_views
from Internships import views as internship_views
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ChinaBack import settings

router = routers.SimpleRouter()
# Quote urls
router.register(r'quotes/random_quote', quotes_views.RandomQuoteView, basename='Quote')

# Internship urls
router.register(r'internships', internship_views.InternshipView, basename='Internship')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)