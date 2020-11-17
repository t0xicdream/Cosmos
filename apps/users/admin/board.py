from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from apps.users.models import Board

# Used to define the representation of the board in the admin panel


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ("name", "description", "period_from", "period_to")

    search_fields = ["user__username"]
