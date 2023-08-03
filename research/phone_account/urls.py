from django.urls import path
from . import views
 
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_detail_view, name='user_detail'),
    path('supplies/', views.supplies_view, name='supplies'), 
    path('success/', views.success_view, name='success'),
    path('history/', views.history_view, name='history'),
]