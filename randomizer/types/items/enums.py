import enum


class ItemShuffleType(enum.Enum):
    """Enumeration for key item types for shuffling."""

    Required = enum.auto()
    Extra = enum.auto()


class ItemUnique(enum.Enum):
    """Enumeration for items that may need to be restricted by how many times they can appear."""

    Always = enum.auto()
    BalancedOnly = enum.auto()
    Never = enum.auto()


class EffectType(enum.Enum):
    Normal = enum.auto()
    ElementalImmunity = enum.auto()
    ElementalResistance = enum.auto()
    StatusProtection = enum.auto()
    FewEffects = enum.auto()
    Buffs = enum.auto()


class EquipStats(str, enum.Enum):
    Speed = "speed"
    Attack = "attack"
    Defense = "defense"
    MagicAttack = "magic_attack"
    MagicDefense = "magic_defense"


class EquipElement(enum.IntEnum):
    Ice = 4
    Thunder = 5
    Fire = 6
    Earth = 7
    Jump = 7


class ItemStatusEffect(enum.IntEnum):
    Mute = 0
    Sleep = 1
    Poison = 2
    Fear = 3
    Berserk = 4
    Mushroom = 5
    Scarecrow = 6
    Invincible = 7


class ItemTempBuff(enum.IntEnum):
    MagicAttack = 3
    Attack = 4
    MagicDefense = 5
    Defense = 6


class ItemTypeValue(enum.IntEnum):
    Weapon = 0b00
    Armor = 0b01
    Accessory = 0b10
    Item = 0b11
