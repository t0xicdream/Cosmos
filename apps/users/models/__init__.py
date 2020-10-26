"""
------
README
------

Be sure to define each model in the database in `__all__`.

Reference: `Django Migration Documentation <https://docs.djangoproject.com/en/3.0/topics/migrations/>`
Reference: `What is __init__.py <https://docs.python.org/3/reference/import.html#regular-packages>`
"""
from .board import Board
from .committee import Committee
from .group_member import GroupMember
from .user import Profile

__all__ = ["Board", "Committee", "Profile", "GroupMember"]
