from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
# from django.contrib.auth.decorators import login_required

# from django.views.generic import TemplateView

# index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phone_account/',include('phone_account.urls')),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    #path('support/',include('support.urls')),
    #path('', include("django.contrib.auth.urls")),
    # path("", login_required(index_view), name="index"),
]
