from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name="index"),
    path('api/get-pizzas', views.api_get_pizzas)
]