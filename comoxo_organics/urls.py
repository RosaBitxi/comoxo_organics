"""comoxo_organics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from comoxo_farm.views import home_page 
from conga_house.views import conga_page
from users.views import sign_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('comoxo/', include(('comoxo_farm.urls', 'home_page'), namespace='comoxo_farm')),
    path('conga/', include(('conga_house.urls', 'conga_page'), namespace='conga_house')),
    path('users/', include(('users.urls', 'dashboard'), namespace='users')),
    path('signin', sign_in, name='sign_in')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)