from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class ScrowBellAttack(EnemyAttack):
    _index = 34
    _name = " S'crow Bell"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.SCARECROW]


__all__ = ["ScrowBellAttack"]
