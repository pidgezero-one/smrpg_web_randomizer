from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class GetToughAttack(EnemyAttack):
    _index = 110
    _name = ' Get Tough!'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(5), TempStatBuff(6)]


__all__ = ["GetToughAttack"]
