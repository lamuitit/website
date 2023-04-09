from django.urls import path
from . import views

urlpatterns = [
#path("<int:id>", views.index, name='index'),
path('', views.index, name='index'),
path('/', views.index, name='index'),
path('home/', views.index, name='home'),
path('camera/', views.camera, name='camera'),
#path('huongdan', views.huongdan, name='huongdan'),
]