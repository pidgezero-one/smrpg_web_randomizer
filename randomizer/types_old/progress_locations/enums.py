"""Enums supporting shuffle progression."""

from enum import Enum, auto


class LocationWorldArea(Enum):
    """Overarching world areas for specific progress locations
    to belong to."""

    MARIOS_PAD = auto()
    MUSHROOM_WAY = auto()
    MUSHROOM_KINGDOM = auto()
    MUSHROOM_KINGDOM_OCCUPIED_ONLY = auto()
    BANDITS_WAY = auto()
    KERO_SEWERS = auto()
    MIDAS_RIVER = auto()
    TADPOLE_POND = auto()
    ROSE_WAY = auto()
    ROSE_TOWN = auto()
    ROSE_TOWN_CLOUDS = auto()
    FOREST_MAZE = auto()
    MOLEVILLE = auto()
    MOLEVILLE_MINES = auto()
    BOOSTER_PASS = auto()
    BOOSTER_TOWER = auto()
    BOOSTER_HILL = auto()
    PIPE_VAULT = auto()
    YOSTER_ISLE = auto()
    MARRYMORE = auto()
    STAR_HILL = auto()
    SEASIDE_TOWN = auto()
    SEA = auto()
    SUNKEN_SHIP = auto()
    LANDS_END = auto()
    BELOME_TEMPLE = auto()
    MONSTRO_TOWN = auto()
    CASINO = auto()
    BEAN_VALLEY = auto()
    NIMBUS_LAND = auto()
    NIMBUS_CASTLE = auto()
    BARREL_VOLCANO = auto()
    BOWSERS_KEEP = auto()
    FACTORY = auto()
    INNER_FACTORY = auto()


class PacketType(Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    FALLING = auto()
    STATIC = auto()
    CHEST = auto()
