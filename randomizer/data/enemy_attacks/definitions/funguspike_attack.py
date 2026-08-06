from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class FunguspikeAttack(EnemyAttack):
    _index = 19
    _name = ' Funguspike'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.MUSHROOM]


__all__ = ["FunguspikeAttack"]
