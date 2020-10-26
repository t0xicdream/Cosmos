from django.urls import path

from . import views

# This file is used to configure the URLs for the app users
# The URL dispatcher allows the user to access the different user views
# https://docs.djangoproject.com/en/3.1/topics/http/urls/

app_name = "cosmos_users"

urlpatterns = [
    path("register/", views.register, name="user_register"),
    path("profile/", views.profile, name="user_profile"),
    path("delete/", views.delete, name="user_delete"),
]
