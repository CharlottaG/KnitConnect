from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatternList.as_view(), name='patterns'),
    path('add_pattern/', views.add_pattern, name='add_pattern'),
]