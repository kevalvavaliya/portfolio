"""protfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from website import views
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from django.urls import path, include  # new
from django.views.static import serve
from django.shortcuts import redirect


def redirect_to_index(request, path=''):
    """Redirect any unmatched URL to the index page"""
    return redirect('index')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("ping/", views.ping, name="ping"),
    # Catch-all patterns - must be last
    re_path(r'^.*/$', redirect_to_index, name='catch_all_slash'),
    re_path(r'^.+$', redirect_to_index, name='catch_all_no_slash'),
]
