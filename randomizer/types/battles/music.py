"""Class instances of battle music."""

from .types import Music


class NormalBattleMusic(Music):
    """The music that plays in most battles in the original game."""

    _name: str = "Regular encounter theme"
    _value: int = 0x00


class MidbossMusic(Music):
    """The music that plays in mid-boss battles in the original game."""

    _name: str = "Midboss theme"
    _value: int = 0x04


class BossMusic(Music):
    """The music that plays in battles with Smithy's henchmen in the original game."""

    _name: str = "Smithy Gang theme"
    _value: int = 0x08


class Smithy1Music(Music):
    """The music that plays during phase 1 of the Smithy fight in the original game."""

    _name: str = "Smithy phase 1 theme"
    _value: int = 0x0C


class CulexMusic(Music):
    """The music that plays during the Culex fight in the original game."""

    _name: str = "Final Fantasy 4 boss theme"
    _value: int = 0x1C


class CorndillyMusic(Music):
    """Minecart music, which can be used as a battle theme."""

    _name: str = "Moleville Minecart theme"
    _value: int = 0x10


def get_default_music():
    """Returns a list of every battle music class."""
    return [
        NormalBattleMusic(),
        MidbossMusic(),
        BossMusic(),
        Smithy1Music(),
        CulexMusic(),
        CorndillyMusic(),
    ]
