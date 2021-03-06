"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView, PasswordResetView, LogoutView
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('refugio.apps.adopcion.urls'), name='home'),
    path('mascota/', include('refugio.apps.mascota.urls')),
    path('usuario/', include('refugio.apps.usuario.urls')),
    path('accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('reset/password_reset_done',
         PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('reset/password_reset_complete',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
