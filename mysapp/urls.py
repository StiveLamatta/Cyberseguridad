from django.urls import path
from . import views

urlpatterns=[
    path("", views.saludo),
    path("test", views.test)
]