from django.urls import path
from django.conf.urls import url

from users import views

app_name = 'users'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signout/', views.sign_out, name='sign_out'),
    path('signin/', views.sign_in, name='sign_in'),
    path('review/add', views.review_add, name='review_add'),
    path('review/update', views.review_update, name='review_update'),
    path('thanks/', views.thank_you, name='thank_you'),
    
]