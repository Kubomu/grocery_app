from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"),
    path('login/', auth_views.LoginView.as_view(template_name = 'admin_app/login.html'), name = 'login'),
    
    
]
