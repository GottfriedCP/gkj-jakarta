from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),

    path('loginx/', views.login_view, name='login'),
    path('logoutx/', views.logout_view, name='logout'),
]
