from django.urls import path

from . import views

urlpatterns=[
    path('home/', views.homepage, name='Home'),
    path('info/', views.infopage, name='Info'),
    path('birth/', views.birthpage, name='Birthday'),
]