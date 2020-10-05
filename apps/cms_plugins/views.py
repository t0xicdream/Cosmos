from django.shortcuts import get_object_or_404, render

from apps.users.models import Board, Committee


def board_subpage(request, board_name):
    # TODO consider adding field "slug"
    board = get_object_or_404(Board, display_name=board_name)
    return render(request, "cms/board_subpage.html", {"board": board})


def committee_subpage(request, committee):
    # TODO consider adding field "slug"
    comm = get_object_or_404(Committee, display_name=committee)
    return render(request, "cms/committee_subpage.html", {"committee": comm})
