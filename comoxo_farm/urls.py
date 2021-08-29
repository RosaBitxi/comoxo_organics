from django.urls import path
from django.conf.urls import url

from comoxo_farm import views

app_name = 'comoxo_farm'
urlpatterns = [
    path('', views.home_page, name='comoxo'),
    
]