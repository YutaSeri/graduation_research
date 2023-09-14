from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('phone/',include('phone.urls')),
   path('beginner/',include('beginner.urls')),
   path('', LoginView.as_view(template_name='phone/login.html'), name='login'),    
]