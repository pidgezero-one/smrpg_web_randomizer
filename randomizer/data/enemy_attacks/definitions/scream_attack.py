from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class ScreamAttack(EnemyAttack):
    _index = 65
    _name = ' Scream'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.FEAR]


__all__ = ["ScreamAttack"]
