from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class EerieJigAttack(EnemyAttack):
    _index = 76
    _name = ' Eerie Jig'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 99
    _status_effects = [Status.SCARECROW]


__all__ = ["EerieJigAttack"]
