from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class ScrowFangsAttack(EnemyAttack):
    _index = 127
    _name = " S'crow Fangs"
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 85
    _status_effects = [Status.SCARECROW]


__all__ = ["ScrowFangsAttack"]
