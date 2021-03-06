from django.urls import path

from . import views

app_name = "cosmos_users"

urlpatterns = [
    path("register/", views.register, name="user_register"),
    path("profile/", views.process_profile_form, name="user_profile"),
    path("delete/", views.delete, name="user_delete"),
]
