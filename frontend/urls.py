

from django.urls import path
from frontend import views



app_name = 'frontend'




urlpatterns = [
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('register', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activateEmail', views.activateEmail, name='activateEmail'),
    path('custom_login', views.custom_login, name='custom_login'),
    path('custom_logout', views.custom_logout, name='custom_logout'),
    path('confirm-logout', views.confirm_logout, name='confirm_logout'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('password_change', views.password_change, name='password_change'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),


]
