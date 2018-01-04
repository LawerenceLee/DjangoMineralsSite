from django.urls import path

from . import views


# app_name needs to be set in order to server static files.
app_name = 'catalog'
urlpatterns = [
    path('random', views.random, name="random"),
    path('<str:mineral_name>', views.detail, name="detail"),
    path('', views.index, name="index"),
]
