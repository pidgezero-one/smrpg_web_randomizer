"""Static values for item properties"""

import enum


class ItemShuffleType(enum.Enum):
    """Enumeration for key item types for shuffling."""

    REQUIRED = enum.auto()
    EXTRA = enum.auto()


class ItemUnique(enum.Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    ALWAYS = enum.auto()
    BALANCED_ONLY = enum.auto()
    NEVER = enum.auto()


class EffectType(enum.Enum):
    """Enumeration to describe the type of effect an item will have on its target."""
    NORMAL = enum.auto()
    ELEMENTAL_IMMUNITY = enum.auto()
    ELEMENTAL_RESISTANCE = enum.auto()
    STATUS_PROTECTION = enum.auto()
    FEW_EFFECTS = enum.auto()
    BUFFS = enum.auto()


class EquipStats(str, enum.Enum):
    """Enumeration for numerical stats that are directly affected by equips."""
    SPEED = "speed"
    ATTACK = "attack"
    DEFENSE = "defense"
    MAGIC_ATTACK = "magic_attack"
    MAGIC_DEFENSE = "magic_defense"


class ItemTempBuff(enum.IntEnum):
    """Enumeration for in-battle temporary buffs applies to offensive and defensive stats."""
    MAGIC_ATTACK = 3
    ATTACK = 4
    MAGIC_DEFENSE = 5
    DEFENSE = 6


class ItemTypeValue(enum.IntEnum):
    """Enumeration for distinct base classifications for items."""
    WEAPON = 0b00
    ARMOR = 0b01
    ACCESSORY = 0b10
    ITEM = 0b11
