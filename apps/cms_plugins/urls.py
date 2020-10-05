from django.urls import path
from . import views

app_name = "cosmos_cms_plugins"

urlpatterns = [
    path("board/<board_name>/", views.board_subpage, name="import_user"),
    path("committee/<committee>/", views.committee_subpage, name="import_user"),
]
