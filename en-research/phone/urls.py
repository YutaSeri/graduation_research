from django.urls import path
from . import views
 
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('edit_basic_info/',views.edit_basic_info_view,name='edit_basic_info'),
    path('users/', views.user_detail_view, name='user_detail'),
    path('supplies/', views.supplies_view, name='supplies'), 
    path('p_success/', views.p_success_view, name='p_success'),
    path('history/', views.history_view, name='history'),
    path('p_requests/', views.p_requests_view, name='p_requests'),
    path('update/',views.update_view,name='update'),
    path('response/',views.response_view,name='response'),
    path('response/<int:bulletin_id>/', views.response_detail, name='response_detail'),
    path('base/',views.base_view,name='base'),
]