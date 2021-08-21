

class Music:
    name = ""
    value = 0


class NormalBattleMusic(Music):
    name = "Regular encounter theme"
    value = 0x00


class MidbossMusic(Music):
    name = "Midboss theme"
    value = 0x04


class BossMusic(Music):
    name = "Smithy Gang theme"
    value = 0x08


class Smithy1Music(Music):
    name = "Smithy phase 1 theme"
    value = 0x0c


class CulexMusic(Music):
    name = "Final Fantasy 4 boss theme"
    value = 0x1c


class CorndillyMusic(Music):
    name = "Moleville Minecart theme"
    value = 0x10

# ********************* Default objects for world


def get_default_music():
    return [
        NormalBattleMusic(),
        MidbossMusic(),
        BossMusic(),
        Smithy1Music(),
        CulexMusic(),
        CorndillyMusic()
    ]
