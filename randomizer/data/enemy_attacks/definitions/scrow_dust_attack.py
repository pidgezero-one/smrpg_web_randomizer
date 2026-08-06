from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class ScrowDustAttack(EnemyAttack):
    _index = 53
    _name = " S'crow Dust"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SCARECROW]


__all__ = ["ScrowDustAttack"]
