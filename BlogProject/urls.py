"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from User import views as Userviews
from WebPage import views as Webviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Webviews.root, name='root'),
    path('index/', Webviews.index, name='index'),
    path('login/', Userviews.Login.as_view(), name='login'),
    path('register/', Userviews.Register.as_view(), name='register'),

    path('user/', include(('User.urls', 'User'), namespace='user')),
    path('blog/', include(('WebPage.urls', 'WebPage'), namespace='blog')),

]
