from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.ProfilesList.as_view(), name='profiles'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('<str:username>/', views.user_profile, name='user_profile'),
]