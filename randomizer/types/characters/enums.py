from enum import Enum


class LevelStats(str, Enum):
    MaxHP = "max_hp"
    Attack = "attack"
    Defense = "defense"
    MagicAttack = "magic_attack"
    MagicDefense = "magic_defense"
