from django.urls import path
from smartphone import views

urlpatterns=[
    path('', views.list_smartphone, name="list-manufacturers"),
    path('register_smartphone/', views.create_smartphone, name="register_smartphone")
]