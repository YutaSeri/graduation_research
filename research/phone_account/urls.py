from django.urls import path
from . import views
 
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('initial/', views.initial_view, name='initial'),
    path('test/', views.test_view, name='test'),
]