from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class GunkBallAttack(EnemyAttack):
    _index = 38
    _name = ' Gunk Ball'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95
    _status_effects = [Status.MUTE]


__all__ = ["GunkBallAttack"]
