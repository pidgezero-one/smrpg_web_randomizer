from .music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CulexMusic,
    CorndillyMusic,
)


# ********************* Default objects for world


def get_default_music():
    return [
        NormalBattleMusic(),
        MidbossMusic(),
        BossMusic(),
        Smithy1Music(),
        CulexMusic(),
        CorndillyMusic(),
    ]
