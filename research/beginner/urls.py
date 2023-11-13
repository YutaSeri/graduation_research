from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home_view, name='home'),
  path('search/', views.search_view, name='search'),
  path('search/results/', views.search_results_view, name='search_results'),
  path('requests1/', views.requests1_view, name='requests1'),
  path('requests2/', views.requests2_view, name='requests2'),
  path('success/', views.success_view, name='success'),
  path('supplie1/', views.supplie1_view, name='supplie1'),
  path('supplie2/', views.supplie2_view, name='supplie2'),
  path('supplie/medical/', views.supplie_medical_view, name='supplie_medical'),
  path('supplie/grocery/', views.supplie_grocery_view, name='supplie_grocery'),
  path('supplie/baby/', views.supplie_baby_view, name='supplie_baby'),
  path('supplie/other/', views.supplie_other_view, name='supplie_other'),
  path('supplie/medical/crutch/', views.supplie_medical_crutch_view, name='supplie_medical_crutch'),
  path('supplie/medical/wheelchair/', views.supplie_medical_wheelchair_view, name='supplie_medical_wheelchair'),
  path('supplie/medical/walker/', views.supplie_medical_walker_view, name='supplie_medical_walker'),
  path('supplie/medical/adult_diapers/', views.supplie_medical_adult_diapers_view, name='supplie_medical_adult_diapers'),
  path('supplie/other/clothes/', views.supplie_other_clothes_view, name='supplie_other_clothes'),
  path('supplie/other/clothes/jacket/', views.supplie_other_clothes_jacket_view, name='supplie_other_clothes_jacket'),
  path('supplie/other/clothes/pants/', views.supplie_other_clothes_pants_view, name='supplie_other_clothes_pants'),
  path('supplie/other/shoes', views.supplie_other_shoes_view, name='supplie_other_shoes'), 
  path('confirm/', views.confirm_view, name='confirm'),  
]
