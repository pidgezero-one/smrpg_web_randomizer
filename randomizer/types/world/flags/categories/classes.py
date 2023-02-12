from typing import List
from randomizer.types.world.flags.classes import Flag


class FlagCategory:
    _id: str = ""
    _name: str = ""
    _subcategories: "List[FlagCategory]" = []
    _flags: List[Flag] = []
    _size: int = 3

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def subcategories(self) -> "List[FlagCategory]":
        return self._subcategories

    @property
    def flags(self) -> List[Flag]:
        return self._flags

    @property
    def size(self) -> int:
        return self._size


class Preset:
    _name: str = ""
    _description: str = ""
    _flags: str = ""

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def flags(self) -> str:
        return self._flags

    @classmethod
    def id(cls):
        return cls.__name__
