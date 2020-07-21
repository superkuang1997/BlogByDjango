from django.urls import path
from WebPage import views


urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('article/', views.article, name='article'),
    path('message/', views.message, name='message'),
    path('diary/', views.diary, name='diary'),



]