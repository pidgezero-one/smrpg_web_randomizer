from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class VigorupAttack(EnemyAttack):
    _index = 123
    _name = ' Vigor up!'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(3), TempStatBuff(4)]


__all__ = ["VigorupAttack"]
