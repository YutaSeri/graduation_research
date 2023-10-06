from django.urls import path
from . import views
 
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_detail_view, name='user_detail'),
    path('supplies/', views.supplies_view, name='supplies'), 
    path('p_success/', views.p_success_view, name='p_success'),
    path('history/', views.history_view, name='history'),
    path('p_requests/', views.p_requests_view, name='p_requests'),
    path('edit_basic_info/',views.edit_basic_info,name='edit_basic_info'),
    path('response/',views.response_view,name='response'),
    path('base/',views.base_view,name='base'),
]