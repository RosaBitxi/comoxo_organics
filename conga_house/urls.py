from django.urls import path
from django.conf.urls import url
from conga_house import views

app_name = 'conga_house'
urlpatterns = [
    path('', views.conga_page, name='conga_page'),
    
]