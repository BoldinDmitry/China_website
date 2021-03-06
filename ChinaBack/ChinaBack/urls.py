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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from ChinaBack import settings
from Headings import views as headings_views
from Internships import views as internship_views
from News import views as news_views
from Quotes import views as quotes_views

router = routers.SimpleRouter()

# Quote urls
router.register(r"quotes/random_quote", quotes_views.RandomQuoteView, basename="Quote")

# Internship urls
router.register(r"internships", internship_views.InternshipView, basename="Internship")

# Heading urls
router.register(r"headings", headings_views.HeadingsView, basename="Heading")
router.register(r"headings_authors", headings_views.AuthorView, basename="Author")

# News urls
router.register(r"news", news_views.NewsView, basename="News")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("djrichtextfield/", include("djrichtextfield.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
