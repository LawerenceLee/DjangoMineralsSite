from django.urls import path

from . import views


# app_name needs to be set in order to server static files.
app_name = 'catalog'
urlpatterns = [
    path('', views.index, name="index"),
]
