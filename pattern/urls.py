from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatternList.as_view(), name='patterns'),
]