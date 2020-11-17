from django.contrib import admin

from apps.users.models import Committee

# Used to define the representation of committees in the admin panel


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "board")

    search_fields = ["user__username", "board"]
