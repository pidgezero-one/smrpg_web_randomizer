from enum import IntEnum


class SpellType(IntEnum):
    Damage = 0
    Heal = 1


class EffectType(IntEnum):
    Inflict = 2
    Nullify = 4


class SpellElement(IntEnum):
    NoElement = 0x00
    Ice = 0x10
    Thunder = 0x20
    Fire = 0x40
    Earth = 0x80
    Jump = 0x80


class InflictFunction(IntEnum):
    Scan = 0
    Miss = 1
    NoDmg = 2
    Revive = 3
    IncJump = 4


class SpellStatusEffects(IntEnum):
    Mute = 0
    Sleep = 1
    Poison = 2
    Fear = 3
    Berserk = 4
    Mushroom = 5
    Scarecrow = 6
    Invincible = 7


class SpellBoosts(IntEnum):
    MagicAttack = 3
    Attack = 4
    MagicDefense = 5
    Defense = 6
