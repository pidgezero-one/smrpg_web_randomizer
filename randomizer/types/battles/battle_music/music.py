"""Class instances of battle music."""

from randomizer.types.battles.battle_music.classes import Music


class NormalBattleMusic(Music):
    """The music that plays in most battles in the original game."""

    name = "Regular encounter theme"
    value = 0x00


class MidbossMusic(Music):
    """The music that plays in mid-boss battles in the original game."""

    name = "Midboss theme"
    value = 0x04


class BossMusic(Music):
    """The music that plays in battles with Smithy's henchmen in the original game."""

    name = "Smithy Gang theme"
    value = 0x08


class Smithy1Music(Music):
    """The music that plays during phase 1 of the Smithy fight in the original game."""

    name = "Smithy phase 1 theme"
    value = 0x0C


class CulexMusic(Music):
    """The music that plays during the Culex fight in the original game."""

    name = "Final Fantasy 4 boss theme"
    value = 0x1C


class CorndillyMusic(Music):
    """Minecart music, which can be used as a battle theme."""

    name = "Moleville Minecart theme"
    value = 0x10
