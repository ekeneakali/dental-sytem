

from django.urls import path
from frontend import views



app_name = 'frontend'




urlpatterns = [
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('register', views.register, name='register'),
    path('custom_login', views.custom_login, name='custom_login'),
    path('custom_logout', views.custom_logout, name='custom_logout'),
    path('confirm-logout', views.confirm_logout, name='confirm_logout'),
    path('detail/<int:id>/', views.detail, name='detail'),



]
