from django.urls import path
from . import views

urlpatterns = [
#path("<int:id>", views.index, name='index'),
path('', views.index, name='index'),
path('/', views.index, name='index'),
path('home/', views.index, name='home'),
path('camera/', views.camera, name='camera'),
path('dslr/', views.dslr, name='dslr'),
path('mirrorless/', views.mirrorless, name='mirrorless'),
path('login/', views.login, name='login'),
path('canon750D', views.canon750D, name='canon750D'),
path('introduction', views.introduction, name='introduction'),
path('contact', views.contact, name='contact'),
path('container', views.container, name='container'),
#path('huongdan', views.huongdan, name='huongdan'),
]