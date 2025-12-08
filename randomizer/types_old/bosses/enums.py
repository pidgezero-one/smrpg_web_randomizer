"""Enums relevant to boss shuffling."""

from enum import Enum, IntEnum, auto

from randomizer.types.battles.types import Music
from randomizer.types.battles import (
    BossMusic,
    CorndillyMusic,
    CulexMusic,
    MidbossMusic,
    NormalBattleMusic,
    Smithy1Music)
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
