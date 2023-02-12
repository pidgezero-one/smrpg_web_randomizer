from .classes import Music


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
    value = 0x0C


class CulexMusic(Music):
    name = "Final Fantasy 4 boss theme"
    value = 0x1C


class CorndillyMusic(Music):
    name = "Moleville Minecart theme"
    value = 0x10
