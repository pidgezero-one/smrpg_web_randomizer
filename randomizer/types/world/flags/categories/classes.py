"""Base classes for settings."""

from typing import List
from randomizer.types.world.flags.classes import Flag


class FlagCategory:
    """Base class for a collection of settings."""

    _id: str = ""
    _name: str = ""
    _subcategories: "List[FlagCategory]" = []
    _flags: List[Flag] = []
    _size: int = 3

    @property
    def id(self) -> str:
        """An identifier for this collection to use internally."""
        return self._id

    @property
    def name(self) -> str:
        """An identifier for this collection to appear in the frontend."""
        return self._name

    @property
    def subcategories(self) -> "List[FlagCategory]":
        """Subcategories for this collection."""
        return self._subcategories

    @property
    def flags(self) -> List[Flag]:
        """Individual settings that belong in this collection."""
        return self._flags

    @property
    def size(self) -> int:
        """Something to do with the frontend that I don't remember"""
        return self._size


class Preset:
    """A pre-created settings string"""

    _name: str = ""
    _description: str = ""
    _flags: str = ""

    @property
    def name(self) -> str:
        """The name of this preset as it appears on the site"""
        return self._name

    @property
    def description(self) -> str:
        """A brief description of who this preset is meant for and what it does"""
        return self._description

    @property
    def flags(self) -> str:
        """The string that corresponds to the desired settings"""
        return self._flags

    @classmethod
    def id(cls):
        """An identifier for this preset to use internally."""
        return cls.__name__
