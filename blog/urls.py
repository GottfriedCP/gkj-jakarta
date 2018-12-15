from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:year>/<slug:slug>/', views.article, name='article'),
    path('<int:year>/<slug:slug>/edit/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('list/', views.list_all, name='list'),
    
    path('', views.index, name='index'),
]
