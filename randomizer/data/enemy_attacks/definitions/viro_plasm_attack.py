from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class ViroPlasmAttack(EnemyAttack):
    _index = 48
    _name = ' Viro Plasm'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.POISON]


__all__ = ["ViroPlasmAttack"]
