from django.urls import path
from . import views

app_name = 'warta'
urlpatterns = [
    path('list/', views.index, name='list'),
    path('create/', views.create, name='create'),
]
