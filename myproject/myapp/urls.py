from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration_form/', views.registration_form, name='registration_form')
]
