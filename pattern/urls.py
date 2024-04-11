from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatternList.as_view(), name='patterns'),
    path('add_pattern/', views.add_pattern, name='add_pattern'),
    path('my_page/', views.my_page, name='my_page'),
    path('<slug:slug>/', views.pattern_details, name='pattern_details'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('pattern/<slug:slug>/', views.like_pattern, name='like_pattern'),
]