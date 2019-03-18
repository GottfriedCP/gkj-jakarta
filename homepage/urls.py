from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),

    path('announcement/<id>/', views.announcement, name='ann'),
    path('create-announcement/', views.create_announcement, name='create_ann'),
    path('edit-announcement/<id>/', views.edit_announcement, name='edit_ann'),

    path('loginx/', views.login_view, name='login'),
    path('logoutx/', views.logout_view, name='logout'),
]
