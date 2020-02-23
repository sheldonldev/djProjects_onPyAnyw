"""mysite URL Configuration

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

import os

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # login
    path('accounts/', include('django.contrib.auth.urls')),

    # home
    path('', TemplateView.as_view(template_name='home/main.html')),

    # apps
    path('polls/', include('polls.urls')),
    path('hello/', include('hello.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
]

# serve static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')
urlpatterns += [
    url(
        r'^site(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
]
