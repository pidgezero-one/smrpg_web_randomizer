from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class SleepSauceAttack(EnemyAttack):
    _index = 41
    _name = ' Sleep-Sauce'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 95
    _status_effects = [Status.SLEEP]


__all__ = ["SleepSauceAttack"]
