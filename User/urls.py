from django.urls import path

from User import views

urlpatterns = [
    path('QQlogin/', views.QQlogin.as_view(), name='QQlogin'),
    path('logout/', views.logout, name='logout'),
]
