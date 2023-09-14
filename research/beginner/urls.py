from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home_view, name='home'),
  path('search/', views.search_view, name='search'),
  path('search/results/', views.search_results_view, name='search_results'),
  path('supplie/', views.supplie_view, name='supplie'),
  path('success/', views.success_view, name='success'),
  path('item/', views.item_view, name='item'),
  path('requests/', views.requests_view, name='requests'),
  path('other_requests/', views.other_requests_view, name='other_requests'),
]
