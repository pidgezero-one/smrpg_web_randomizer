from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class Attack47(EnemyAttack):
    _index = 47
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90
    _status_effects = [Status.FEAR]


__all__ = ["Attack47"]
