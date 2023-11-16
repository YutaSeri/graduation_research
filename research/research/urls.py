from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

def has_permission(request):
   return request.account.is_active

admin.site.site_header = '避難者個別物資要望管理システム'


urlpatterns = [
   path('admin/', admin.site.urls),
   path('adminer/',include('adminer.urls')),
   path('phone/',include('phone.urls')),
   path('beginner/',include('beginner.urls')),
   path('', LoginView.as_view(template_name='phone/login.html'), name='login'),    
]