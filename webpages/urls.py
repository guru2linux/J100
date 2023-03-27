from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about-us/', views.about_us, name='about_us'),
    path('lodge-officers/', views.lodge_officers, name='lodge_officers'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('send_email/', views.send_email, name='send_email'),
    path('success/', views.success, name='success'),
]