"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from Student import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create),
    path('display/', views.display),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('create_form/', views.create_form),
    path('update_form/<int:id>/', views.update_form),
    path('registration/', views.registration),
    path('login/', views.login_view),
    path('logout/', views.signout),
    path('create_img/', views.create_form_img),

    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
