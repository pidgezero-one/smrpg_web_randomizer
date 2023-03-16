"""Helper functions related to battle music."""

from randomizer.types.battles.battle_music.music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CulexMusic,
    CorndillyMusic,
)


# ********************* Default objects for world


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
