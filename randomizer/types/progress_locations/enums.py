from enum import Enum, auto


class LocationWorldArea(Enum):
    MariosPad = auto()
    MushroomWay = auto()
    MushroomKingdom = auto()
    MushroomKingdomOccupiedOnly = auto()
    BanditsWay = auto()
    KeroSewers = auto()
    MidasRiver = auto()
    TadpolePond = auto()
    RoseWay = auto()
    RoseTown = auto()
    RoseTownClouds = auto()
    ForestMaze = auto()
    Moleville = auto()
    MolevilleMines = auto()
    BoosterPass = auto()
    BoosterTower = auto()
    BoosterHill = auto()
    PipeVault = auto()
    YosterIsle = auto()
    Marrymore = auto()
    StarHill = auto()
    SeasideTown = auto()
    Sea = auto()
    SunkenShip = auto()
    LandsEnd = auto()
    BelomeTemple = auto()
    MonstroTown = auto()
    Casino = auto()
    BeanValley = auto()
    NimbusLand = auto()
    NimbusCastle = auto()
    BarrelVolcano = auto()
    BowsersKeep = auto()
    Factory = auto()
    InnerFactory = auto()


class PacketType(Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    Falling = auto()
    Static = auto()
    Chest = auto()
