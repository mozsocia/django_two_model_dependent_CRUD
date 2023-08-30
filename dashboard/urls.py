from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('create_sale/', views.create_sale, name='create_sale'),
]
