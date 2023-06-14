from django.urls import path
from . import views

urlpatterns = [
  path('first_view/', views.first_view, name='firstview'),
  path('second_view/', views.second_view, name='secondview'),
  path('third_view/', views.third_view, name='thirdview'),
  path('fourth_view/', views.fourth_view, name='fourthview'),
]