from django.contrib import admin
from django.urls import path
from appcad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
]
