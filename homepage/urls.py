from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('loginx/', views.login_view, name='login'),
    path('logoutx/', views.logout_view, name='logout'),
]
