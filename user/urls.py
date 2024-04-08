from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.ProfilesList.as_view(), name='profiles_list'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('<slug:slug>/', views.user_profile, name="user_profile"),
]