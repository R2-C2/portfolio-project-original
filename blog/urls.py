from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name = "detail"),
]
