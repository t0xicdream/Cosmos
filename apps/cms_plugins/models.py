from cms.plugin_base import CMSPlugin
from django.db import models
from django.db.models import CASCADE

from apps.users.models import Board, Committee


class CommitteeListPluginModel(CMSPlugin):
    committees = models.ManyToManyField(Committee)
    button = models.BooleanField(default=True, verbose_name="use button")

    @property
    def sorted_committees(self):
        return self.committees.all().order_by("display_name")

    def copy_relations(self, oldinstance):
        self.committees.set(oldinstance.committees.all())

    def __str__(self):
        return "CommitteeList:".join(committee.name for committee in self.committees.all())


class BoardListPluginModel(CMSPlugin):
    boards = models.ManyToManyField(Board)

    @property
    def sorted_boards(self):
        return self.boards.all().order_by("-group__name")

    def copy_relations(self, oldinstance):
        self.boards.set(oldinstance.boards.all())

    def __str__(self):
        return "BoardList:".join(board.name for board in self.boards.all())


class TextImagePluginModel(CMSPlugin):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=400)
    Button = models.BooleanField(default=False, verbose_name="use button")
    ButtonLink = models.URLField(blank=True)
    ButtonText = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="cardImg", default="img/default.jpg")
    orientation = models.BooleanField(default=False, verbose_name="image on the left")

    def __str__(self):
        return "TextImageCard:" + self.title


class CommitteeSubpageTitlePluginModel(CMSPlugin):
    committee = models.OneToOneField(Committee, on_delete=CASCADE)

    def copy_relations(self, old_instance):
        self.committee.set(old_instance.committee.all())

    def __str__(self):
        return f"CommitteeSubpage: {self.committee.name}"


class BoardSubpageTitlePluginModel(CMSPlugin):
    board = models.OneToOneField(Board, on_delete=CASCADE)

    def copy_relations(self, old_instance):
        self.board.set(old_instance.board.all())

    def __str__(self):
        return f"CommitteeSubpage: {self.board.name}"