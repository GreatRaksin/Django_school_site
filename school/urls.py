from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutors/', views.tutors, name='tutors'),
    path('dopolnitelnie-zanyatia/', views.extra_lessons, name='dop'),
]