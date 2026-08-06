from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class SporocystAttack(EnemyAttack):
    _index = 54
    _name = ' Sporocyst'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUSHROOM]


__all__ = ["SporocystAttack"]
