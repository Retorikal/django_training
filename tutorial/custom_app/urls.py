from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:number>', views.number, name='number'),
    path('template/', views.template, name='number'),
    path('example0/', views.example0, name='exp0'),
    path('example1/', views.example1, name='exp1'),
    path('example2/', views.example2, name='exp2'),
]
