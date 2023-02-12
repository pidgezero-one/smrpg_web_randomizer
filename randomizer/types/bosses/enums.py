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
    MushroomWay = "Mushroom Way (Hammer Bros)"
    BanditsWay = "Bandit's Way (Croco 1)"
    MushroomKingdom = "Mushroom Kingdom (Mack)"
    Mimic1 = "First mimic chest (originally in Kero Sewers, Pandorite)"
    KeroSewers = "End of Kero Sewers (Belome 1)"
    ForestMaze = "Forest Maze (Bowyer)"
    MinesMidboss = "Moleville Mines trampoline area (Croco 2)"
    MinesEnd = "End of Moleville Mines (Punchinello)"
    TowerCurtain = "Booster Tower curtains area (Booster)"
    TowerBalcony = "Booster Tower balcony (Knife Guy & Grate Guy)"
    Marrymore = "Marrymore (Bundt)"
    SunkenShipMidboss = "Sunken Ship password door (King Calamari)"
    Mimic2 = "Second mimic chest (originally in Sunken Ship, Hidon)"
    SunkenShipEnd = "End of Sunken Ship (Johnny)"
    SeasideTown = "Seaside Town (Yaridovich)"
    LandsEndCloud = "Land's End random cloud spawn (Mokura)"
    BelomeTemple = "Belome Temple (Belome 2)"
    Dojo1 = "First Monstro Town Dojo challenge (Jagger)"
    Dojo2 = "Second Monstro Town Dojo challenge (Jinx 1)"
    Dojo3 = "Third Monstro Town Dojo challenge (Jinx 2)"
    Dojo4 = "Fourth Monstro Town Dojo challenge (Jinx 3)"
    MonstroDoor = "Monstro Town sealed door (Culex)"
    Mimic3 = "Third mimic chest (originally in Bean Valley, Box Boy)"
    BeanValley = "Bean Valley planter (Megasmilax)"
    NimbusStatues = "Nimbus Castle statue room (Dodo)"
    GiantEgg = "Nimbus Castle giant egg room (Birdetta)"
    NimbusEnd = "End of Nimbus Castle (Valentina)"
    BarrelVolcanoMidboss = "Barrel Volcano bridge area (Czar Dragon)"
    BarrelVolcanoEnd = "End of Barrel Volcano (Axem Rangers)"
    BowsersKeepObstacles = "Bowser's Keep battle room (Chester)"
    BowsersKeepMidboss = "End of Bowser's Keep obstacle course (Magikoopa)"
    BowsersKeepEnd1 = "End of Bowser's Keep, first boss (Boomer)"
    BowsersKeepEnd2 = "End of Bowser's Keep, second boss (Exor)"
    FactoryMidboss = "Early Outer Factory (Count Down)"
    FactoryEnd = "End of Outer Factory (Cloaker & Domino)"
    InnerFactory1 = "Inner Factory entrance (Clerk)"
    InnerFactory2 = "Inner Factory second room (Manager)"
    InnerFactory3 = "Inner Factory third room (Director)"
    InnerFactory4 = "End of Inner Factory (Gunyolk)"
    InnerFactoryLair = "Inner Factory lair (Smithy)"


class Battlefields(IntEnum):
    """Enumeration for ID values for battlefields."""

    Forest = 0x00
    Bowyer = 0x01
    Beanstalks = 0x02
    KingCalamari = 0x03
    SunkenShip = 0x04
    MolevilleMines = 0x05
    BowsersKeep = 0x07
    CzarDragon = 0x08
    MushroomWay = 0x09
    Mountains = 0x0A
    House = 0x0B
    BoosterTower = 0x0C
    MushroomKingdom = 0x0D
    Underwater = 0x0E
    MushroomKingdomThroneRoom = 0x0F
    Exor = 0x10
    ClownBros = 0x11
    Countdown = 0x12
    Gate = 0x13
    Volcano = 0x14
    KeroSewers = 0x15
    NimbusCastle = 0x16
    Birdetta = 0x17
    Valentina = 0x18
    Underground = 0x19
    MushroomKingdomOutside = 0x1C
    Boomer = 0x1D
    Plateau = 0x21
    SeaEnclave = 0x22
    Bundt = 0x23
    StarHill = 0x24
    Yaridovich = 0x25
    Sea = 0x26
    AxemRangers = 0x27
    CloakerDomino = 0x28
    BeanValley = 0x29
    BelomeTemple = 0x2A
    Desert = 0x2B
    Smithy = 0x2C
    SmithyFinal = 0x2D
    JinxDojo = 0x2E
    Culex = 0x2F
    Factory = 0x30
    BeanValleyUnderground = 0x31


class BattleMusic(Music, Enum):
    """Enumeration for ID values for battle music."""

    Normal = NormalBattleMusic
    Boss1 = MidbossMusic
    Boss2 = BossMusic
    Smithy = Smithy1Music
    Culex = CulexMusic
    Corn = CorndillyMusic


class HenchmanType(Enum):
    Boss = auto()
    Pack = auto()
    Event = auto()
    ExternalEvent = auto()
    NPCOnly = auto()


class SpriteSize(Enum):
    Small = auto()
    Large = auto()
    Attack = auto()
