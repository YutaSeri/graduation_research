from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home_view, name='home'),
  path('supplies/', views.supplies_view, name='supplies'),
  path('success/', views.success_view, name='success'),
  path('item/', views.item_view, name='item'),
  path('requests/', views.requests_view, name='requests'),
  path('other_requests/', views.other_requests_view, name='other_requests'),
]