"""Static values for item properties"""

import enum


class ItemShuffleType(enum.Enum):
    """Enumeration for key item types for shuffling."""

    REQUIRED = enum.auto()
    EXTRA = enum.auto()


class ItemUnique(enum.Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    ALWAYS = enum.auto()
    BALANCED_ONLY = enum.auto()
    NEVER = enum.auto()
