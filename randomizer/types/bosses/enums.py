"""Enums relevant to boss shuffling."""

from enum import Enum, IntEnum, auto
from randomizer.types.battles.battle_music.classes import Music
from randomizer.types.battles.battle_music.music import (
    BossMusic,
    CorndillyMusic,
    CulexMusic,
    MidbossMusic,
    NormalBattleMusic,
    Smithy1Music,
)
from randomizer.types.world.flags.enums import FlagOptions


class BossLocations(FlagOptions):
    """List of boss location names, used to create the list of star piece exclusion options."""

    MUSHROOM_WAY = "Mushroom Way (Hammer Bros)"
    BANDITS_WAY = "Bandit's Way (Croco 1)"
    MUSHROOM_KINGDOM = "Mushroom Kingdom (Mack)"
    MIMIC_1 = "First mimic chest (originally in Kero Sewers, Pandorite)"
    KERO_SEWERS = "End of Kero Sewers (Belome 1)"
    FOREST_MAZE = "Forest Maze (Bowyer)"
    MINES_MIDBOSS = "Moleville Mines trampoline area (Croco 2)"
    MINES_END = "End of Moleville Mines (Punchinello)"
    TOWER_CURTAIN = "Booster Tower curtains area (Booster)"
    TOWER_BALCONY = "Booster Tower balcony (Knife Guy & Grate Guy)"
    MARRYMORE = "Marrymore (Bundt)"
    SUNKEN_SHIP_MIDBOSS = "Sunken Ship password door (King Calamari)"
    MIMIC_2 = "Second mimic chest (originally in Sunken Ship, Hidon)"
    SUNKEN_SHIP_END = "End of Sunken Ship (Johnny)"
    SEASIDE_TOWN = "Seaside Town (Yaridovich)"
    LANDS_END_CLOUD = "Land's End random cloud spawn (Mokura)"
    BELOME_TEMPLE = "Belome Temple (Belome 2)"
    DOJO_1 = "First Monstro Town Dojo challenge (Jagger)"
    DOJO_2 = "Second Monstro Town Dojo challenge (Jinx 1)"
    DOJO_3 = "Third Monstro Town Dojo challenge (Jinx 2)"
    DOJO_4 = "Fourth Monstro Town Dojo challenge (Jinx 3)"
    MONSTRO_DOOR = "Monstro Town sealed door (Culex)"
    MIMIC_3 = "Third mimic chest (originally in Bean Valley, Box Boy)"
    BEAN_VALLEY = "Bean Valley planter (Megasmilax)"
    NIMBUS_STATUES = "Nimbus Castle statue room (Dodo)"
    GIANT_EGG = "Nimbus Castle giant egg room (Birdetta)"
    NIMBUS_END = "End of Nimbus Castle (Valentina)"
    BARREL_VOLCANO_MIDBOSS = "Barrel Volcano bridge area (Czar Dragon)"
    BARREL_VOLCANO_END = "End of Barrel Volcano (Axem Rangers)"
    BOWSERS_KEEP_OBSTACLES = "Bowser's Keep battle room (Chester)"
    BOWSERS_KEEP_MIDBOSS = "End of Bowser's Keep obstacle course (Magikoopa)"
    BOWSERS_KEEP_END_1 = "End of Bowser's Keep, first boss (Boomer)"
    BOWSERS_KEEP_END_2 = "End of Bowser's Keep, second boss (Exor)"
    FACTORY_MIDBOSS = "Early Outer Factory (Count Down)"
    FACTORY_END = "End of Outer Factory (Cloaker & Domino)"
    INNER_FACTORY_1 = "Inner Factory entrance (Clerk)"
    INNER_FACTORY_2 = "Inner Factory second room (Manager)"
    INNER_FACTORY_3 = "Inner Factory third room (Director)"
    INNER_FACTORY_4 = "End of Inner Factory (Gunyolk)"
    INNER_FACTORY_LAIR = "Inner Factory lair (Smithy)"


class Battlefields(IntEnum):
    """Enumeration for ID values for battlefields."""

    FOREST = 0x00
    BOWYER = 0x01
    BEANSTALKS = 0x02
    KING_CALAMARI = 0x03
    SUNKEN_SHIP = 0x04
    MOLEVILLE_MINES = 0x05
    BOWSERS_KEEP = 0x07
    CZAR_DRAGON = 0x08
    MUSHROOM_WAY = 0x09
    MOUNTAINS = 0x0A
    HOUSE = 0x0B
    BOOSTER_TOWER = 0x0C
    MUSHROOM_KINGDOM = 0x0D
    UNDERWATER = 0x0E
    MUSHROOM_KINGDOM_THRONE_ROOM = 0x0F
    EXOR = 0x10
    CLOWN_BROS = 0x11
    COUNTDOWN = 0x12
    GATE = 0x13
    VOLCANO = 0x14
    KERO_SEWERS = 0x15
    NIMBUS_CASTLE = 0x16
    BIRDETTA = 0x17
    VALENTINA = 0x18
    UNDERGROUND = 0x19
    MUSHROOM_KINGDOM_OUTSIDE = 0x1C
    BOOMER = 0x1D
    PLATEAU = 0x21
    SEA_ENCLAVE = 0x22
    BUNDT = 0x23
    STAR_HILL = 0x24
    YARIDOVICH = 0x25
    SEA = 0x26
    AXEM_RANGERS = 0x27
    CLOAKER_DOMINO = 0x28
    BEAN_VALLEY = 0x29
    BELOME_TEMPLE = 0x2A
    DESERT = 0x2B
    SMITHY = 0x2C
    SMITHY_FINAL = 0x2D
    JINX_DOJO = 0x2E
    CULEX = 0x2F
    FACTORY = 0x30
    BEAN_VALLEY_UNDERGROUND = 0x31


class BattleMusic(Music, Enum):
    """Enumeration for ID values for battle music."""

    NORMAL = NormalBattleMusic
    BOSS_1 = MidbossMusic
    BOSS_2 = BossMusic
    SMITHY = Smithy1Music
    CULEX = CulexMusic
    CORN = CorndillyMusic


class HenchmanType(Enum):
    """Enumeration to indicate how information about the henchman should be used."""

    BOSS = auto()
    PACK = auto()
    EVENT = auto()
    EXTERNAL_EVENT = auto()
    NPC_ONLY = auto()


class SpriteSize(Enum):
    """Enumeration to indicate the expected sprite type for a boss NPC."""

    SMALL = auto()
    LARGE = auto()
    ATTACK = auto()
